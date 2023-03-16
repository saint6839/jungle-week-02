import sys

N = int(sys.stdin.readline())
values = list(map(int,sys.stdin.readline().split()))

values.sort()

lt = 0
rt = len(values) - 1

closest = sys.maxsize
results = [0, 0]

while lt < rt:
    sum = values[lt] + values[rt]

    if sum == 0:
        results[0] = values[lt]
        results[1] = values[rt]
        break

    if abs(sum) < closest:
        closest = abs(sum)
        results[0] = values[lt]
        results[1] = values[rt]
        if closest == 0:
            break

    if sum < 0:
        lt += 1
    else:
        rt -= 1

print(results[0], results[1])