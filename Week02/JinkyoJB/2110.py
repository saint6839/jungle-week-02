import sys
input = sys.stdin.readline
# 집의 개수(N)와 공유기의 개수(C)를 입력 받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력 받기
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()  # 이진 탐색 수행을 위해 정렬 수행

start = 1  # 가능한 최소 거리(min gap)
end = arr[-1] - arr[0]  # 가능한 최대 거리(max gap)
result = 0

while (start <= end):
    mid = (start+end)//2
    #공유기 설치 변수
    value = arr[0]
    count = 1 # 일단 첫번째는 기본으로 설치
    for i in range(1,n): #집마다
        if arr[i] >= value+mid: #mid를 기준으로 판단: i집과 1번집의 거리가 기준mid이상이면 설치, i+1과 i집의 거리가 기준mid이상이면 설치..반복
            value= arr[i]
            count+=1 #공유기 몇개 설치했는지 기록
    if count >= c:  # mid를 기준으로 판단:2 #설치해야되는 공유기가 남았으면 거리기준이 너무 작은거임. 키우자. start +1
        start = mid +1
        result = mid
    else:
        end = mid -1 
print(result)
