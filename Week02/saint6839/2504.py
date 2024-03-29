import sys

inputs = sys.stdin.readline().strip()

stack = []
result = 0
temp = 1

isRight = True
for i in range(len(inputs)):
    if inputs[i] == '(':
        stack.append(inputs[i])
        temp *= 2
    elif inputs[i] == '[':
        stack.append((inputs[i]))
        temp *= 3
    elif inputs[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if inputs[i-1] == '(':
            result += temp
        stack.pop()
        temp /= 2
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if inputs[i-1] == '[':
            result += temp
        stack.pop()
        temp /= 3

if stack:
    print(0)
else:
    print(int(result))


