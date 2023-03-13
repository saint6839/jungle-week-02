import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
compare_numbers = list(map(int, sys.stdin.readline().split()))

results = dict()

for number in numbers:
    results.setdefault(number, 1)

for compare_number in compare_numbers:
    results.setdefault(compare_number, 0)
    print(results[compare_number])
