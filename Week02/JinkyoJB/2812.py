import sys
from collections import deque

input = sys.stdin.readline
#input
a,k =(map(int,input().split()))
datas = list(map(int, input().rstrip()))  # [1, 9, 2, 4]

#처리용 덱, output변수
stacks = []

input = sys.stdin.readline

for number in datas:
    while stacks and stacks[-1] < number and k > 0:
        stacks.pop()
        k -= 1
    stacks.append(number)
if k > 0:
    print(''.join(map(str,stacks[:-k])))
else:
    print(''.join(map(str,stacks)))



