import sys

N, K = map(int, sys.stdin.readline().split())

value = sys.stdin.readline().strip()

stack = []
count = 0
for i in range(N):
    while stack:
        if count == K:
            break
        if stack[-1] >= int(value[i]):
            break
        stack.pop()
        count += 1

    stack.append(int(value[i]))

for i in range(N-K):
    print(stack[i], end='')