import sys

N = int(sys.stdin.readline())
boards = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0
def dfs(x, y, N):
    global white
    global blue
    for i in range(x, x+N):
        for j in range(y, y+N):
            if boards[x][y] != boards[i][j]:
                dfs(x, y, N//2)
                dfs(x+N//2, y, N//2)
                dfs(x, y+N//2, N//2)
                dfs(x+N//2, y+N//2, N//2)
                return

    if boards[x][y] == 1:
        blue += 1
    else:
        white += 1

dfs(0, 0, N)

print(white)
print(blue)
