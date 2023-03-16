import sys
input = sys.stdin.readline
from heapq import *

left_heap=[]
right_heap=[]

n = int(input())
for i in range(n):
    input_n = int(input())
    if len(left_heap)==len(right_heap):
        heappush(left_heap, (-input_n, input_n)) #최대우선순위 큐
    else:
        heappush(right_heap, (input_n, input_n)) #최소 우선순위 큐

    if right_heap and left_heap[0][1] > right_heap[0][0]: 
        min=heappop(right_heap)[0]
        max=heappop(left_heap)[1]
        heappush(left_heap, (-min, min))
        heappush(right_heap, (max,max))
    print(left_heap[0][1])
""" 만약에 leftheap의 루트가 rightheap의 루트보다 크면 left와 right의 루트를 바꿔준다.
left는 중간값을 기준으로 작은 수가 들어가는 곳이다. 그런데 leftheap의 루트가 right보다 크다면,
중간값보다 큰수가 leftheap에 들어가 있는 상황이기에 leftheap과 rightheap의 루트를 바꿔준다.
"""

