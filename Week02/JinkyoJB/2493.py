import sys

input = sys.stdin.readline

n=(int(input()))
arr = list(map(int, input().split()))  # [6, 9, 5, 7, 4]

stacks=[] #arr하나씩 꺼내면서 저장하면서 결과값에 참고할 덱
result=[0]*n #결과값: 왼쪽에서 가장 큰 수

for i in range(n): 
    while stacks: 
        if arr[i]> stacks[-1][0]:#현재 탐색하고 있는 탑의 높이가 stack top보다 크다면
            stacks.pop() #그 stacks에 탑제거
        else:  # 현재 탐색하고 있는 탑의 높이가 stack top보다 작다면
            result[i] = stacks[-1][1] #그 때의 값을 result에 저장
            break
    stacks.append([arr[i],i+1])

for i in result:
    print(i, end=' ')
#print(*result)