import sys

inputs = sys.stdin.readline()

stack = []
temp = 1
sum = 0
for i in range(len(inputs)):
    input = inputs[i]

    if input == '(':
        stack.append(input)
        temp *= 2
    elif input == '[':
        stack.append(input)
        temp *= 3
    elif input == ')':
        if not stack or inputs[i-1] == '[':
            sum = 0
            break
        elif inputs[i-1] == '(':
            sum += temp
        stack.pop()
        temp /= 2
    elif input == ']':
        if not stack or inputs[i-1] == '(':
            sum = 0
            break
        elif inputs[i-1] == '[':
            sum += temp
        stack.pop()
        temp /= 3
print(int(sum))