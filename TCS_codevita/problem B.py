import heapq

n = int(input())
orders = [tuple(map(int, input().split())) + (i,) for i in range(n)]  # (arr, dur, vip, idx)

# sort by arrival time so we push arrivals in chronological order
orders.sort(key=lambda x: x[0])

waiting = []
time = 0
i = 0
events = []  # (time, delta) for waiting intervals: +1 at arrival, -1 at start_of_service

while i < n or waiting:
    if not waiting and i < n:
        time = max(time, orders[i][0])
    while i < n and orders[i][0] <= time:
        arr, dur, vip, idx = orders[i]
        # heap order: vip first (vip=1), then arrival time (FCFS), then shorter duration for same arrival
        heapq.heappush(waiting, (-vip, arr, dur, idx))
        i += 1
    if waiting:
        neg_vip, arr, dur, idx = heapq.heappop(waiting)
        start = max(time, arr)
        if start > arr:
            # person waited from arr (inclusive) until start (exclusive)
            events.append((arr, 1))
            events.append((start, -1))
        time = start + dur

# sweep-line to find max concurrent waiting people
events.sort(key=lambda x: (x[0], x[1]))  # ensure -1 processed before +1 at same time if needed
current = 0
max_chairs = 0
for t, delta in events:
    current += delta
    max_chairs = max(max_chairs, current)

print(max_chairs, end="")
