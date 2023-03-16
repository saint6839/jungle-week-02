import sys

input = sys.stdin.readline

n = int(input())
stacks = [ int(input()) for i in range(n)]
result = 1
pivot_num = stacks.pop()
for _ in range(n-1):
    a = stacks.pop()
    if a > pivot_num:
        pivot_num = a
        result +=1

print(result)