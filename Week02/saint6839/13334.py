import sys
import heapq

N = int(sys.stdin.readline())
possible_positions = []
positions = []

for _ in range(N):
    positions.append(sorted(list(map(int, sys.stdin.readline().split()))))
d = int(sys.stdin.readline())

for position in positions:
    start, end = position
    if end - start <= d:
        possible_positions.append(position)

possible_positions.sort(key= lambda x: x[1])

priority_queue = []
result = 0
for possible_position in possible_positions:
    if not priority_queue:
        heapq.heappush(priority_queue, possible_position)
    else:
        while priority_queue[0][0] < possible_position[1] - d:
            heapq.heappop(priority_queue)
            if not priority_queue:
                break
        heapq.heappush(priority_queue, possible_position)
    result = max(result, len(priority_queue))

print(result)