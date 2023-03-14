import sys

N, M = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

lt = 0
rt = max(heights)

result = 0
while lt <= rt:
    mid = (lt + rt) // 2

    sum = 0
    for height in heights:
        if height > mid:
            sum += height - mid

    if sum >= M:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(result)
