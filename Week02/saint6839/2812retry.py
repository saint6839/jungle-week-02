import sys

N, K = map(int, sys.stdin.readline().split())

stack = []
results = []


value = sys.stdin.readline()

count = 0

for i in range(N):
    while stack:
        if stack[-1] >= int(value[i]):
            break
        if count == K:
            break
        stack.pop()
        count += 1

    stack.append(int(value[i]))

for i in range(N-K):
    print(stack[i], end='')
