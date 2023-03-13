import sys
import heapq

N = int(sys.stdin.readline())

priority_queue = []
for _ in range(N):
    heapq.heappush(priority_queue, int(sys.stdin.readline()))

sum = 0

while len(priority_queue) > 1:
    temp = heapq.heappop(priority_queue) + heapq.heappop(priority_queue)
    sum += temp
    heapq.heappush(priority_queue, temp)

print(sum)