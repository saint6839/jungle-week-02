import sys

# input = sys.stdin.readline

arr=[1,1,0,1,1,3]

max_deck = [[1, 0]] #크기 비교를 쉽게하기 위해 처음에 1,1칸짜리 놓기
result=[]
len_arr = len(arr)

#a[0]의 max deck만들기
for i in range(1,len_arr): #i는 arr의 인덱스
    # max_deck의 top과 현재탐색값 비교, 크면 저장.
    if (max_deck[-1][0] <= arr[i]):
        max_deck.append([arr[i],i])
print('max_deck', max_deck)  # [[2, 1], [4, 3], [5, 4]]

len_max_deck = len(max_deck)
# 세워서 셀건지
how_long = 0
a_max = max_deck[-1][0]

while len(max_deck) >= 2:
    a, b = max_deck.pop()
    print(a,b)
    if b - max_deck[-1][1] == 1:  # pop한것과 deck의 top의 인덱스 비교: index차이가 1이라면, result에 결과값넣기
        a_max = max(a_max, max_deck[-1][0])
        print('a_max', a_max)
        how_long +=1
        print('how_long', how_long)
    else:
        result.append([a_max, how_long])
else:
    result.append([a_max, how_long])

print('result',result)


#누워서 셀건지
