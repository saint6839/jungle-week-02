import sys
from collections import deque

n = int(input())
arr = deque([i+1 for i in range(n)])

for i in range(n-1):
    arr.popleft()
    arr.rotate(-1)

print(*arr)