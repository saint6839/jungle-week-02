import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    stacks=[]
    data = input().strip()
    for j in data:
        if j == "(":
            stacks.append(j)
        else:
            if stacks:
                stacks.pop()
            else:
                print('NO')
                break
    else:
        if stacks:
            print('NO')
        else:
            print('YES')




# for _ in range(n):
#     sum = 0
#     data = input().strip()
#     for i in data:
#         if i == "(":
#             sum += 1
#         else:
#             sum-=1
#             if sum<0:
#                 print('NO')
#                 break
#     if sum == 0:
#         print('YES')
#     elif sum>0:
#         print('NO')
