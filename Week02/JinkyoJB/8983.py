import sys
input = sys.stdin.readline

m,n,l = list(map(int, input().split()))
sa_list = list(map(int, input().split()))
sa_list.sort()
animal = [list(map(int, input().split())) for i in range(n)]
animal = list(filter(lambda x: x[1] <= l, animal))
print(m, n, l)  # 4 8 4
print(sa_list)  # [1, 4, 6, 9]
print(animal) #[[7, 2], [3, 3], [4, 5], [5, 1], [2, 2], [1, 4], [8, 4], [9, 4]]

log_arr=[0]*n
for i,a in enumerate(animal): #animal요소를 기준으로
    start=0
    end = m-1  # 탐색 범위는 사대
    while start<=end:
        mid=(start+end)//2
        value = abs(sa_list[mid]-a[0])+a[1]
        if value <= l:
            start = mid +1
            log_arr[i]=1
            break
        else:
            end = mid - 1
print(sum(log_arr))
