import sys
from collections import defaultdict

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
it = iter(data)
n = int(next(it))

# Store edges and build grid
edges = defaultdict(set)
xs = set()
ys = set()

for _ in range(n):
    x1, y1, x2, y2 = map(int, [next(it) for _ in range(4)])
    if x1 == x2:  # vertical line
        y1, y2 = min(y1, y2), max(y1, y2)
        for y in range(y1, y2):
            edges[(x1, y)].add((x1, y+1))
            edges[(x1, y+1)].add((x1, y))
    else:  # horizontal line
        x1, x2 = min(x1, x2), max(x1, x2)
        for x in range(x1, x2):
            edges[(x, y1)].add((x+1, y1))
            edges[(x+1, y1)].add((x, y1))
    xs.update([x1, x2])
    ys.update([y1, y2])

if not xs or not ys:
    print(0)
    sys.exit(0)

# Find connected components (squares)
def find_square(x, y):
    if not all((x, y) in edges and (x+1, y) in edges and 
               (x, y+1) in edges and (x+1, y+1) in edges):
        return False
    
    points = [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]
    for p1 in points:
        neighbors = 0
        for p2 in points:
            if p2 in edges[p1]:
                neighbors += 1
        if neighbors != 2:  # Each corner should connect to exactly 2 others
            return False
    return True

squares = []
for x in range(min(xs), max(xs)):
    for y in range(min(ys), max(ys)):
        if find_square(x, y):
            squares.append((x, y))

if not squares:
    print(0)
    sys.exit(0)

# Calculate possible box dimensions
area = len(squares)

def can_form_box(l, w, h):
    if 2*(l*w + w*h + h*l) != area:
        return False
        
    # Try to match faces
    faces = [(l,w), (l,w), (w,h), (w,h), (h,l), (h,l)]
    used = set()
    
    def find_face(height, width, used_squares):
        for x, y in squares:
            if (x, y) in used_squares:
                continue
            if x + width > max(xs) or y + height > max(ys):
                continue
            
            valid = True
            curr_squares = set()
            for i in range(height):
                for j in range(width):
                    if (x+j, y+i) not in squares:
                        valid = False
                        break
                    curr_squares.add((x+j, y+i))
                if not valid:
                    break
                    
            if valid and not (curr_squares & used_squares):
                return curr_squares
        return None

    def try_match(face_idx, used_squares):
        if face_idx == len(faces):
            return True
            
        height, width = faces[face_idx]
        # Try both orientations
        for h, w in [(height, width), (width, height)]:
            face = find_face(h, w, used_squares)
            if face:
                if try_match(face_idx + 1, used_squares | face):
                    return True
        return False
        
    return try_match(0, set())

# Try all possible dimensions
max_dim = int((area/2)**0.5) + 1
max_volume = 0

for l in range(1, max_dim + 1):
    for w in range(1, max_dim + 1):
        for h in range(1, max_dim + 1):
            if can_form_box(l, w, h):
                max_volume = max(max_volume, l * w * h)

print(max_volume)
