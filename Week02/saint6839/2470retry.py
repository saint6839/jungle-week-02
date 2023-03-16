import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

lt = 0
rt = len(numbers) - 1

result = abs(numbers[lt] + numbers[rt])
results = [numbers[lt], numbers[rt]]

while lt < rt:
    sum = numbers[lt] + numbers[rt]

    if sum == 0:
        print(numbers[lt], numbers[rt])

    if abs(sum) < result:
        results[0] = numbers[lt]
        results[1] = numbers[rt]
        result = abs(numbers[lt] + numbers[rt])
        if result == 0:
            break

    if sum < 0:
        lt += 1
    else:
        rt -= 1

print(*results)