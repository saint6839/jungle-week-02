"""
문제 수 찾기

이분탐색
"""
import sys
import bisect

input = sys.stdin.readline

n = int(input()) #5
n_arr = list(map(int, input().split()))  # [4, 1, 5, 2, 3] [1,2,3,4,5]

m = int(input())# 5
m_arr = list(map(int, input().split()))  # [1, 3, 7, 9, 5]

n_arr.sort()


for i in m_arr:
    start = 0
    end = n-1
    while (start <= end):
        pivot = (start +end)//2
        if n_arr[pivot] == i :
            print(1)
            break
        elif n_arr[pivot] > i :
            end = pivot-1
        else:
            start = pivot +1
    else:
        print(0)
        

# def bin_search(a, key):
#     """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
#     pl = 0           # 검색 범위 맨 앞 원소의 인덱스
#     pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스

#     while (pl <= pr):
#         pc = (pl + pr) // 2  # 중앙 원소의 인덱스 #판단 기준!
#         if a[pc] == key:
#             return 1    # 검색 성공
#         elif a[pc] < key:
#             pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
#         else:
#             pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
#     return 0            # 검색 실패

# for i in m_arr:
#     print(bin_search(n_arr,i))


# def count(arr, left, right):
#     left_index = bisect.bisect_left(arr, left)
#     right_index = bisect.bisect_right(arr, right)
#     return right_index-left_index


# for i in m_arr:
#     if count(n_arr, i, i) != 0:
#         print(1)
#     else:
#         print(0)

