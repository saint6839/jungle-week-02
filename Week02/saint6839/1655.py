import sys
import heapq

N = int(sys.stdin.readline())

small_heap = []
large_heap = []

for _ in range(N):
    value = int(sys.stdin.readline())
    if len(small_heap) == len(large_heap):
        heapq.heappush(small_heap, -value)
    else:
        heapq.heappush(large_heap, value)

    if large_heap and -small_heap[0] > large_heap[0]:
        small_popped = -heapq.heappop(small_heap)
        large_popped = -heapq.heappop(large_heap)

        heapq.heappush(small_heap, large_popped)
        heapq.heappush(large_heap, small_popped)

    print(-small_heap[0])
