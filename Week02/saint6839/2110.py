import sys

N, C = map(int, sys.stdin.readline().split())

numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

lt = 1
rt = numbers[-1] - numbers[0]
result = 0

while lt <= rt:
    mid = (lt + rt) // 2
    count = 1
    cur = numbers[0]

    for i in range(1, N):
        if numbers[i] >= cur + mid:
            cur = numbers[i]
            count += 1

    if count >= C:
        lt = mid + 1
        result = mid
    else:
        rt = mid - 1

print(result)