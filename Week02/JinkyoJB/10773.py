import sys

input = sys.stdin.readline

stacks = []

k = int(input())
for _ in range(k):
    a = int(input())
    if a==0:
        stacks.pop()
    else:
        stacks.append(a)
print(sum(stacks))