import sys

N = int(sys.stdin.readline())


bars = []
for _ in range(N):
    bars.append(int(sys.stdin.readline()))

before = bars.pop()
count = 1

while len(bars):
    pop = bars.pop()
    if pop > before:
        before = pop
        count += 1

print(count)
