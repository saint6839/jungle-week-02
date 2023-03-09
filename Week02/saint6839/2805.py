import math
import sys

N, M = map(int, sys.stdin.readline().split())

heights = list(map(int, sys.stdin.readline().split()))

lt = 1
rt = max(heights)

heights.sort()
results = []
while lt <= rt:
    mid = (lt + rt) // 2

    sum = 0
    for height in heights:
        diff = height - mid
        if diff > 0:
            sum += diff
    if sum >= M:
        lt = mid + 1
    if sum < M:
        rt = mid - 1

print(rt)

