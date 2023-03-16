import sys

N = int(sys.stdin.readline())

papers = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

blue = 0
white = 0

def dfs(x, y, n):
    global blue
    global white

    for i in range(x, x+n):
        for j in range(y ,y+n):
            if papers[x][y] != papers[i][j]:
                dfs(x, y, n//2)
                dfs(x, y+n//2, n//2)
                dfs(x+n//2, y, n//2)
                dfs(x+n//2, y+n//2, n//2)
                return

    if papers[x][y]:
        blue += 1
    else:
        white += 1

dfs(0, 0, N)
print(white)
print(blue)