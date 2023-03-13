import sys

K = int(sys.stdin.readline())

numbers = []
for _ in range(K):
    value = int(sys.stdin.readline())

    if not value:
        numbers.pop()
        continue
    numbers.append(value)

print(sum(numbers))
