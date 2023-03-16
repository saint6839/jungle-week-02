import sys
import heapq

input = sys.stdin.readline

n= int(input())
heap=[]

for _ in range(n):
    num= int(input())
    if num==0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -num)

# #insert
# def insert(heap, num):
#     heap.append(num)

#     i=len(heap)-1
#     while i > 1: #heap의 노드가 1개 이상 있을 때 진행해라
#         if heap[i] >heap[i//2]: #i=0이면 루트노드
#             tmp = heap[i]
#             heap[i] = heap[i//2]
#             heap[i//2] = tmp
#             i = i//2
#         else:
#             break

# #remove
# def remove(heap):
#     maxVal= heap[1]
#     tmp = heap.pop()

#     parent =1
#     child=2
    
#     while child <= len(heap)-1:
#         if child < len(heap)-1 and heap[child] < heap[child+1]:
#             child +=1
        
#         if heap[child] <= tmp:
#             break

#         heap[parent] = heap[child]

#         parent = child
#         child*=2

#         if len(heap) != 1:
#             heap[parent] = tmp
#         return maxVal
    
# #main
# n= int(input())

# heap = [0]

# for _ in range(n):
#     num = int(input())

#     if num==0:
#         if len(heap)==1:
#             print(0)
#         else:
#             print(remove(heap))
#     else:
#         insert(heap, num)



