import heapq
import sys

N = int(sys.stdin.readline())

priority_queue = []
for _ in range(N):
    value = int(sys.stdin.readline())

    if value == 0:
        if priority_queue:
            print(-heapq.heappop(priority_queue))
        else:
            print(0)
    else:
        heapq.heappush(priority_queue, -value)
