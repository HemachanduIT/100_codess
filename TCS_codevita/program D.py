import sys
sys.setrecursionlimit(10000)

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
it = iter(data)

N = int(next(it))
names = [next(it) for _ in range(N)]
skills = [int(next(it)) for _ in range(N)]
name_to_idx = {name: i for i, name in enumerate(names)}

N1 = int(next(it))
in_pair = [-1] * N
items = []  # each item: {'members':[idxs], 'weight':w, 'count':c, 'valid':True}
for _ in range(N1):
    a = next(it); b = next(it)
    ia = name_to_idx[a]; ib = name_to_idx[b]
    # create friend-pair item
    items.append({'members':[ia, ib], 'weight': skills[ia] + skills[ib], 'count': 2, 'valid': True})
    pid = len(items) - 1
    in_pair[ia] = pid
    in_pair[ib] = pid

# singles for those not in any friend pair
for i in range(N):
    if in_pair[i] == -1:
        items.append({'members':[i], 'weight': skills[i], 'count': 1, 'valid': True})
        pid = len(items) - 1
        in_pair[i] = pid

# Now read rivals and mark conflicts
N2 = int(next(it))
# build conflict sets between items
M_all = len(items)
conflict = [0] * M_all  # bitmask over item indices
for _ in range(N2):
    a = next(it); b = next(it)
    ia = name_to_idx[a]; ib = name_to_idx[b]
    pa = in_pair[ia]; pb = in_pair[ib]
    if pa == pb:
        # rivals inside same item -> item impossible to select
        items[pa]['valid'] = False
    else:
        # mark mutual conflict
        conflict[pa] |= (1 << pb)
        conflict[pb] |= (1 << pa)

limit = int(next(it))

# Filter only valid items and rebuild indices
old2new = [-1] * M_all
weights = []
counts = []
for old_i, itobj in enumerate(items):
    if not itobj['valid']:
        continue
    new_i = len(weights)
    old2new[old_i] = new_i
    weights.append(itobj['weight'])
    counts.append(itobj['count'])
# rebuild conflict masks in new indexing
M = len(weights)
conflict_mask = [0] * M
for old_i in range(M_all):
    ni = old2new[old_i]
    if ni == -1:
        continue
    cm = conflict[old_i]
    newmask = 0
    b = 0
    while cm:
        if cm & 1:
            if old2new[b] != -1:
                newmask |= (1 << old2new[b])
        cm >>= 1
        b += 1
    conflict_mask[ni] = newmask

# Precompute suffix remaining counts to prune
suffix = [0] * (M + 1)
for i in range(M - 1, -1, -1):
    suffix[i] = suffix[i + 1] + counts[i]

best = 0

def dfs(i, curr_w, curr_cnt, selected_mask):
    global best
    if curr_w > limit:
        return
    if curr_cnt + suffix[i] <= best:
        return
    if i == M:
        if curr_cnt > best:
            best = curr_cnt
        return
    # option: skip i
    dfs(i + 1, curr_w, curr_cnt, selected_mask)
    # option: include i if no conflict and within limit
    if (selected_mask & conflict_mask[i]) == 0 and curr_w + weights[i] <= limit:
        dfs(i + 1, curr_w + weights[i], curr_cnt + counts[i], selected_mask | (1 << i))

dfs(0, 0, 0, 0)
print(best)