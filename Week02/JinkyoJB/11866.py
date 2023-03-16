import sys
from collections import deque

n,k = map(int,input().split())
arr = deque([i+1 for i in range(n)])
result = []

arr.rotate(-(k-1))
while len(arr)>0:
    a = arr.popleft()
    result.append(a)
    arr.rotate(-(k-1))

print('<', end='')
print(*result, sep=', ',end='')
print('>', end='')
