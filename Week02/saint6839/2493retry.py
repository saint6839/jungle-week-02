import sys

N = int(sys.stdin.readline())

heights = list(map(int, sys.stdin.readline().split()))
stack = []
results = []

for i in range(N):
    while stack:
        if stack[-1][1] < heights[i]:
            stack.pop()
        else:
            results.append(stack[-1][0])
            break

    if not stack:
        results.append(0)

    stack.append((i+1, heights[i]))

print(*results)
