import sys

N = int(sys.stdin.readline())

towers = list(map(int, sys.stdin.readline().split()))


stack = []
results = []
for i in range(len(towers)):
    while stack:
        if stack[-1][1] > towers[i]:
            results.append(stack[-1][0] + 1)
            break
        stack.pop()

    if not stack:
        results.append(0)
    stack.append([i, towers[i]])

print(' '.join(map(str, results)))
