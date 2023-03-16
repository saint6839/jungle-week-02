from collections import deque
import sys
# stack의 응용1. 후위표기식 이용!!!!!!!

arr = []
arr.extend(input().strip())

arr_len = len(arr) #홀수면 틀린거
if arr_len%2 == 1:
    print(0)
    sys.exit()

stacks = deque()
result = deque()

for index, i in enumerate(arr): #arr1에 있는 요소를 하나하나씩 꺼내서, 
    if i=='(': #여는 기호가 나오면 stacks에 i, index저장
        stacks.append((i, index))
    elif i == '[':  # 여는 기호가 나오면 stacks에 i, index저장
        stacks.append((i, index))
    elif i ==')': #닫는 기호가 나오면 저장했을 때의 index와이 차이를 계산해서 result 덱에 저장
        try: 
            bi, bindex = stacks.pop()
            if bi != '(':
                sys.exit(0)
            else:
                result.append([2, (index-bindex-1)//2])
        except:
            print(0)
            sys.exit()
    elif i ==']':
        try:
            bi, bindex = stacks.pop()
            if bi != '[':
                sys.exit()
            else:
                result.append([3, (index-bindex-1)//2])
        except:  # stacks[0]에 [가 없다면
            print(0)
            sys.exit()
print(result)
result_len = len(result)
final = []

for i in range(result_len):
    a, b = result.pop()
    if b==0: #[],()처럼 인덱스 차이가 없을 경우는 a값(2 or 3)을 final 리스트에 넣기
        final.append(a)
    elif b>0: #(x),[x]처럼 인덱스 차이가 있을 경우, 인덱스 차이만큼 앞의 요소 들 중, b=0이면 *a, b!=0이면 pass --> 우선순위 계산
        for j in range(1,b+1):
            if result[-j][1] ==0:
                result[-j][0] = result[-j][0]*a  # b=0이면 *a
            else:
                pass

    else:
        print(0)
        sys.exit()

print(sum(final))