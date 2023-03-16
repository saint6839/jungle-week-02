import sys
input=sys.stdin.readline
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start=0
end=max(array)
result=0

while (start<= end):
    mid = (start+end)//2
    sum_val = 0
    for i in array:
        if i > mid:
            sum_val += i-mid
    if sum_val < m:
        end =mid- 1
    else:
        start =mid+ 1
        result = mid
    
print(result)


    
        
