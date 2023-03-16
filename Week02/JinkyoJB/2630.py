import sys

input = sys.stdin.readline

n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]

white,blue = 0 , 0 #초기값 설정

def div_conq(x,y,N): #분할정복
    global white, blue 
    count = 0

    for i in range(x, x+N):
        for j in range(y, y+N):
            if map[i][j]:
                count += 1
    if count==0:
        white += 1
    elif count == N**2:
        blue += 1
    else:
        div_conq(x,y, N//2)
        div_conq(x+N//2, y, N//2)
        div_conq(x, y+N//2, N//2)
        div_conq(x + N // 2, y + N // 2, N // 2)
    return

div_conq(0,0,n)
print(white)
print(blue)
