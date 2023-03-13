import sys
from collections import deque

N = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    row, col = map(int, sys.stdin.readline().split())
    board[row - 1][col - 1] = 2

sec_dir = dict()
L = int(sys.stdin.readline())
for _ in range(L):
    sec, dir = map(str, sys.stdin.readline().strip().split())
    sec_dir[int(sec)] = dir

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque()
x = 0
y = 0
queue.append((x, y))
count = 0
dir_index = 0

while True:
    count += 1
    x = x + dx[dir_index]
    y = y + dy[dir_index]

    if not 0 <= x < N or not 0 <= y < N:
        break

    if board[x][y] == 1:
        break

    if board[x][y] == 0:
        queue.append((x, y))
        board[x][y] = 1
        poppedX, poppedY = queue.popleft()
        board[poppedX][poppedY] = 0
        if count in sec_dir:
            if sec_dir[count] == 'L':
                dir_index = (dir_index - 1) % 4
            elif sec_dir[count] == 'D':
                dir_index = (dir_index + 1) % 4

    if board[x][y] == 2:
        queue.append((x, y))
        board[x][y] = 1
        if count in sec_dir:
            if sec_dir[count] == 'L':
                dir_index = (dir_index - 1) % 4
            elif sec_dir[count] == 'D':
                dir_index = (dir_index + 1) % 4

print(count)
