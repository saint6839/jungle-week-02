import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for i in range(1, N+1):
    queue.append(i)

count = 1
while len(queue) > 1:
    if count % 2 == 0:
        queue.append(queue.popleft())
    else:
        queue.popleft()
    count+=1
print(queue[0])
