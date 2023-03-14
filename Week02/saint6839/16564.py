import sys

N, K = map(int, sys.stdin.readline().split())

levels = []
for i in range(N):
    levels.append(int(sys.stdin.readline()))
levels.sort()

lt = min(levels)
rt = lt + K

result = 0
while lt <= rt:
    mid = (lt + rt) // 2

    sum = 0
    for level in levels:
        if mid > level:
           sum += (mid - level)

    if sum <= K:
        lt = mid + 1
        result = max(result, mid)
    else:
        rt = mid - 1

print(result)