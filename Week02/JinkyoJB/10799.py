import sys
from collections import deque

input = sys.stdin.readline
arr = deque()
arr.extend(enumerate(input().rstrip()))
# deque([(0, '('), (1, ')'), (2, '('), (3, '('), (4, '('), (5, '('), (6, ')'), (7, '('), (8, ')'), (9, ')'), (10, '('), (11, '('), (12, ')'), (13, ')'), (14, '('), (15, ')'), (16, ')'), (17, ')'), (18, '('), (19, '('), (20, ')'), (21, ')')])

stacks = deque()
pop_nx_list = []

for i in arr:
    if i[1]=='(':
        stacks.append(i)
    elif i[1]==')':
        a,b = stacks.pop()
        nx_a = a-1 
        nx_b = b+1
        if nx_a > 0 and nx_a not in pop_nx_list:
            pop_nx_list.append(a)
 

        