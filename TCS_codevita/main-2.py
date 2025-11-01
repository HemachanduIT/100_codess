from collections import deque, defaultdict
from itertools import permutations

def normalize_edges(edges):
    """Make each pair (u, v) ordered and sort the list."""
    normalized = []
    for u, v in edges:
        if u > v:
            u, v = v, u
        normalized.append((u, v))
    normalized.sort()
    return normalized

def encode(edges):
    """Encode edges into a unique string."""
    return ','.join(f"{u}-{v}" for u, v in edges) + ','

def find_cycles(adj, nodes):
    """Find all simple cycles of length >= 3 in the graph."""
    cycles = set()

    def dfs(node, parent, path, visited):
        path.append(node)
        visited.add(node)
        for nxt in adj[node]:
            if nxt == parent:
                continue
            if nxt in visited:
                if nxt in path:
                    cycle = path[path.index(nxt):]
                    if len(cycle) >= 3:
                        # Normalize cycle rotation
                        min_pos = cycle.index(min(cycle))
                        cycle = cycle[min_pos:] + cycle[:min_pos]
                        cycles.add(tuple(cycle))
            elif len(path) < len(nodes):
                dfs(nxt, node, path, visited)
        path.pop()
        visited.remove(node)

    for start in nodes:
        dfs(start, -1, [], set())

    return cycles

def main():
    a = int(input().strip())
    b = [tuple(map(int, input().split())) for _ in range(a)]
    c = [tuple(map(int, input().split())) for _ in range(a)]

    nodes = sorted(set(u for pair in b for u in pair))

    q = normalize_edges(b)
    r = encode(q)
    o = normalize_edges(c)
    p = encode(o)
    if r == p:
        print(0,end="")
        return

    seen = {r: 0}
    queue = deque([(q, 0)])

    while queue:
        u, steps = queue.popleft()

        # Build adjacency
        adj = defaultdict(list)
        for x, y in u:
            adj[x].append(y)
            adj[y].append(x)

        # Find all possible cycles
        z = find_cycles(adj, nodes)

        # Try rotating each cycle
        for cycle in z:
            mapping = {node: node for node in nodes}
            n = len(cycle)
            for i in range(n):
                mapping[cycle[i]] = cycle[(i + 1) % n]
            ar = [(mapping[x], mapping[y]) for x, y in u]
            ar = normalize_edges(ar)
            key = encode(ar)
            if key == p:
                print(steps + 1,end="")
                return
            if key not in seen:
                seen[key] = steps + 1
                queue.append((ar, steps + 1))
    print(-1,end="")

if __name__ == "__main__":
    main()