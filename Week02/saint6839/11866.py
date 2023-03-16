import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque()

for i in range(1, N+1):
    queue.append(i)

results = []

count = 1
while queue:
    popped = queue.popleft()
    if count % K == 0:
        results.append(popped)
        count += 1
        continue
    count += 1
    queue.append(popped)
print('<'+', '.join(map(str, results)) +'>')