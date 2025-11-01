import sys
from collections import deque, defaultdict

def read_input():
    data = sys.stdin.read().splitlines()
    i = 0
    L = len(data)
    while i < L and data[i].strip() == "":
        i += 1
    if i >= L:
        return 0, [], []
    n = int(data[i].strip()); i += 1
    while i < L and data[i].strip() == "":
        i += 1
    if i < L and data[i].strip().lower() == "shuffled":
        i += 1
    shuffled = []
    while len(shuffled) < n and i < L:
        shuffled.append(data[i])
        i += 1
    while i < L and data[i].strip() == "":
        i += 1
    if i < L and data[i].strip().lower() == "original":
        i += 1
    original = []
    while len(original) < n and i < L:
        original.append(data[i])
        i += 1
    return n, shuffled, original

def expand_frontier(queue, dist_this, dist_other):
    for _ in range(len(queue)):
        cur = queue.popleft()
        cur_d = dist_this[cur]
        n = len(cur)
        for i in range(n):
            for j in range(i, n):
                seg = cur[i:j+1]
                rem = cur[:i] + cur[j+1:]
                for k in range(len(rem)+1):
                    if k == i:
                        continue
                    new = rem[:k] + seg + rem[k:]
                    if new in dist_this:
                        continue
                    dist_this[new] = cur_d + 1
                    if new in dist_other:
                        return dist_this[new] + dist_other[new]
                    queue.append(new)
    return None

def min_moves_bidirectional(start, target):
    if start == target:
        return 0
    start_t, target_t = tuple(start), tuple(target)
    q1, q2 = deque([start_t]), deque([target_t])
    d1, d2 = {start_t: 0}, {target_t: 0}
    while q1 and q2:
        if len(q1) <= len(q2):
            steps = expand_frontier(q1, d1, d2)
        else:
            steps = expand_frontier(q2, d2, d1)
        if steps is not None:
            return steps
    return -1

def main():
    n, shuffled, original = read_input()
    if n == 0:
        print(0)
        return
    pos_map = defaultdict(deque)
    for idx, line in enumerate(original):
        pos_map[line].append(idx)
    shuffled_ids = []
    ok = True
    for line in shuffled:
        if not pos_map[line]:
            ok = False
            break
        shuffled_ids.append(pos_map[line].popleft())
    if not ok:
        print(-1)
        return
    target = list(range(n))
    ans = min_moves_bidirectional(shuffled_ids, target)
    print(ans,end="")

if __name__ == "__main__":
    main()
