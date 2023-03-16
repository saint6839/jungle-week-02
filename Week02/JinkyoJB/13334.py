import sys
from heapq import *
# 라인 스위핑 문제 - 우선순위 큐 자주 사용됨.

input = sys.stdin.readline

n = int(input())

# [[10, 20], [10, 25], [25, 30], [25, 35], [5, 40], [30, 50], [50, 60], [80, 100]]
datas = [sorted(list(map(int,input().split()))) for i in range(n)] #[,]안의 요소도 오름차순 정렬
datas.sort(key=lambda x: x[1]) #[0,1] 1요소 기준으로 오름차순 정렬, 철로를 확인할 때 가장 작은 위치부터 확인하기 위해
d = int(input())

checked=[] #길이가 d안에 들어오는 것들만 1차적으로 넣기
for i in datas:
    x,y = i
    if (y-x)<=d: #각 요소의 길이가 주어진 d보다 작은지 확인
        checked.append(i)  # 작으면 heap에 넣기
    
heap=[]
cnt=0

for i in checked:
    if not heap: #heap에 아무것도 없으면
        heappush(heap,i) 
    else:
        while heap[0][0] < i[1]-d: #만약 철로의 길이 밖에 있으면 힙에 존재한는 가장 작은 값 제거
            heappop(heap)
            if not heap:
                break
        heappush(heap,i)
    cnt = max(cnt, len(heap))

print(cnt)
    