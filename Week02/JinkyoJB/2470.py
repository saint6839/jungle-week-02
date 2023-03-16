import sys
input = sys.stdin.readline

n = int(input())
datas = sorted(map(int,input().split()))

opti =2e9+1
result = [0,0]

start = 0  # 탐색값의 오른쪽 데이터부터
end = n-1  # 맨 끝열의 데이터가 초기 탐색범위
while (start < end):
    sum = datas[start] + datas[end] #해당값을 더한 특성값
    if abs(sum) < opti: #그 절대값이 기존 값보다 작으면 그 값으로 업데이트
        opti = abs(sum)
        result = [start, end]  # output을 위해 해당index 저장
    if  sum < 0:  # 음수면 0으로 향해야 하니 mid값을 더 오른 쪽으로 보내기 위해 start를 오른쪽으로
        start += 1
    elif sum == 0: #충족하면 바아로 정답 출력하고 중단
        print(datas[result[0]], datas[result[1]])
        sys.exit()
    elif sum > 0:
        end -=1
        
print(datas[result[0]], datas[result[1]])
