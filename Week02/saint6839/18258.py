import sys
from collections import deque

queue = deque()

N = int(sys.stdin.readline())

for _ in range(N):
    inputs = list(map(str, sys.stdin.readline().strip().split()))
    if inputs[0] == 'push':
        queue.append(int(inputs[1]))
    elif inputs[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif inputs[0] == 'size':
        print(len(queue))
    elif inputs[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif inputs[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif inputs[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
