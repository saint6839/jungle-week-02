import heapq
import sys

N = int(sys.stdin.readline())
lst = dict()
front_queue = []
back_queue = []

for _ in range(N):
    value = int(sys.stdin.readline())
    if len(front_queue) == len(back_queue):
        heapq.heappush(front_queue, -value)
    else:
        heapq.heappush(back_queue, value)

    if back_queue and -front_queue[0] > back_queue[0]:
        front_popped = heapq.heappop(front_queue)
        back_popped = heapq.heappop(back_queue)

        heapq.heappush(front_queue, -back_popped)
        heapq.heappush(back_queue, -front_popped)

    print(-front_queue[0])

