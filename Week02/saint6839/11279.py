import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())


queue = PriorityQueue()
for _ in range(N):
    value = int(sys.stdin.readline())
    if value == 0 and queue.empty():
        print(0)

    if value == 0 and not queue.empty():
        print(-queue.get())
    else:
        queue.put(-value)

