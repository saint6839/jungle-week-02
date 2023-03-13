import sys

N, C = map(int, sys.stdin.readline().split())

positions = []

for _ in range(N):
    positions.append(int(sys.stdin.readline()))

positions.sort()

lt = 1
rt = positions[-1] - positions[0]
result = 0
while lt <= rt:
    mid = (lt + rt) // 2

    count = 1
    now = positions[0]

    for i in range(1, N):
        if positions[i] >= now + mid:
            count += 1
            now = positions[i]

    if count >= C:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(result)