import sys

N, K = map(int, sys.stdin.readline().split())

levels = []
for _ in range(N):
    levels.append(int(sys.stdin.readline()))

levels.sort()

lt = levels[0]
rt = levels[0] + K

result = 0
while lt <= rt:
    mid = (lt + rt) // 2

    sum = 0
    for level in levels:
        if mid > level:
           sum += (mid - level)

    if sum > K:
        rt = mid - 1
    else:
        lt = mid + 1
        result = mid

print(result)