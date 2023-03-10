import sys

N = int(sys.stdin.readline())
results = []

for _ in range(N):
    input = sys.stdin.readline().split()

    if input[0] == 'push':
        results.append(int(input[1]))
    if input[0] == 'top':
        if len(results) == 0:
            print(-1)
        else:
            print(results[len(results) - 1])
    if input[0] == 'size':
        print(len(results))
    if input[0] == 'empty':
        if len(results) == 0:
            print(1)
        else:
            print(0)
    if input[0] == 'pop':
        if len(results) == 0:
            print(-1)
        else:
            print(results.pop())