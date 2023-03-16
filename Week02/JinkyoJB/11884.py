import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]

heapify(arr)

for i in range(0, len(arr),2):
    arr[i]+arr[i+1]
