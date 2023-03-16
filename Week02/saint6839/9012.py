import sys

T = int(sys.stdin.readline())

for _ in range(T):
    inputs = sys.stdin.readline().strip()
    stack = []

    isVPS = True

    for input in inputs:
        if input == '(':
            stack.append(input)
        else:
            if not len(stack):
                isVPS = False
                break
            else:
                stack.pop()

    if len(stack) or not isVPS:
        print('NO')
    else:
        print('YES')
