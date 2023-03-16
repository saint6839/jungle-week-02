"""
이분탐색
end란 탐색해야하는 범위의 끝값
mid에 장난질
* (mid - 레벨) : 팀목표레벨이 mid일 때 각캐릭터가 몇레벨을 올렸는지
"""
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = [int(input()) for i in range(n)]  # [10, 15, 20]
arr.sort()

start = arr[0]
end = arr[0]+m
result = 0
while (start <= end):
    mid = (start+end)//2
    sum = 0
    for i in range(0,n):
        if mid-arr[i]>0:
            sum += mid-arr[i] 
    if sum <= m:  # 팀목표레벨이 mid일 때 총 몇 레벨을 올려야하는지, 적으면 기준 올리기
        start = mid +1
        result = mid
    else:
        end = mid-1

print(result)