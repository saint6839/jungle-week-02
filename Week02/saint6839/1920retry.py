import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
compare_numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()


for compare_number in compare_numbers:

    lt = 0
    rt = len(numbers) - 1
    isExists = False

    while lt <= rt:
        mid = (lt + rt) // 2

        if numbers[mid] == compare_number:
            isExists = True
            print(1)
            break

        if numbers[mid] > compare_number:
            rt = mid - 1
        else:
            lt = mid + 1

    if not isExists:
        print(0)