# 🧩 Box Game – Rubik’s Cube Fault Detection
# Unique rewritten structure with full rule support

def clone(c):
    return {f: [r[:] for r in c[f]] for f in c}

def read_faces(n):
    sides = ["base", "back", "top", "front", "left", "right"]
    cube = {}
    for s in sides:
        cube[s] = [input().split() for _ in range(n)]
    return cube

def rotate_90(face):
    return [list(x) for x in zip(*face[::-1])]

def rotate_270(face):
    return [list(x) for x in zip(*face)][::-1]

def is_uniform(face):
    c = face[0][0]
    return all(x == c for row in face for x in row)

# ---------- Major Cube Moves ----------
def turn_left(c):
    c["front"], c["left"], c["back"], c["right"] = (
        c["right"], c["front"], c["left"], c["back"]
    )
    c["top"] = rotate_90(c["top"])
    c["base"] = rotate_270(c["base"])

def turn_right(c):
    c["front"], c["right"], c["back"], c["left"] = (
        c["left"], c["front"], c["right"], c["back"]
    )
    c["top"] = rotate_270(c["top"])
    c["base"] = rotate_90(c["base"])

def rot_front(c):
    c["front"], c["base"], c["back"], c["top"] = (
        c["top"], c["front"], c["base"], c["back"]
    )
    c["left"] = rotate_90(c["left"])
    c["right"] = rotate_270(c["right"])

def rot_back(c):
    c["front"], c["top"], c["back"], c["base"] = (
        c["base"], c["front"], c["top"], c["back"]
    )
    c["left"] = rotate_270(c["left"])
    c["right"] = rotate_90(c["right"])

def rot_left(c):
    c["top"], c["left"], c["base"], c["right"] = (
        c["right"], c["top"], c["left"], c["base"]
    )
    c["front"] = rotate_270(c["front"])
    c["back"] = rotate_90(c["back"])

def rot_right(c):
    c["top"], c["right"], c["base"], c["left"] = (
        c["left"], c["top"], c["right"], c["base"]
    )
    c["front"] = rotate_90(c["front"])
    c["back"] = rotate_270(c["back"])

# ---------- Fault Detection ----------
def is_faulty(cube):
    counts = {}
    for f in cube.values():
        for row in f:
            for col in row:
                counts[col] = counts.get(col, 0) + 1
    mx = max(counts.values())
    return sum(counts.values()) - mx == 1

def is_solved(cube):
    return any(is_uniform(f) for f in cube.values())

# ---------- Minor Row/Column Moves ----------
def shift_face_row(face, idx, dirn):
    n = len(face)
    if dirn == "left":
        face[idx] = face[idx][1:] + [face[idx][0]]
    else:
        face[idx] = [face[idx][-1]] + face[idx][:-1]

def shift_face_col(face, idx, dirn):
    n = len(face)
    col = [face[i][idx] for i in range(n)]
    if dirn == "up":
        col = col[1:] + [col[0]]
    else:
        col = [col[-1]] + col[:-1]
    for i in range(n):
        face[i][idx] = col[i]

# ---------- Instruction Execution ----------
def perform(c, cmd):
    parts = cmd.split()
    if parts[0] == "turn":
        if parts[1] == "left":
            turn_left(c)
        else:
            turn_right(c)
    elif parts[0] == "rotate":
        if parts[1] == "front":
            rot_front(c)
        elif parts[1] == "back":
            rot_back(c)
        elif parts[1] == "left":
            rot_left(c)
        elif parts[1] == "right":
            rot_right(c)
    else:
        side, pos, direction = parts[0], int(parts[1]) - 1, parts[2]
        if direction in ("left", "right"):
            shift_face_row(c[side], pos, direction)
        else:
            shift_face_col(c[side], pos, direction)
    return c

# ---------- Main ----------
def main():
    n, k = map(int, input().split())
    cube = read_faces(n)
    instructions = [input().strip() for _ in range(k)]

    for i in range(k):
        temp = clone(cube)
        for j in range(k):
            if i == j:
                continue
            temp = perform(temp, instructions[j])
        if is_solved(temp):
            if is_faulty(cube):
                print("Faulty")
            print(instructions[i])
            return
    print("Not Possible")

if __name__ == "__main__":
    main()
