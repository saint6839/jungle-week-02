import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    row, col = map(int, sys.stdin.readline().split())
    board[row-1][col-1] = 2


L = int(sys.stdin.readline())
sec_dir = dict()
for _ in range(L):
    sec, dir = map(str, sys.stdin.readline().split())
    sec_dir[int(sec)] = dir

queue = deque()

dRow = [0, 1, 0, -1]
dCol = [1, 0, -1, 0]
dir_index = 0

row = 0
col = 0
queue.append((row, col))
board[row][col] = 1
result = 0

while True:
    result += 1
    row = row + dRow[dir_index]
    col = col + dCol[dir_index]

    if not 0 <= row < N or not 0 <= col < N:
        break

    if board[row][col] == 1:
        break

    if board[row][col] == 0:
        board[row][col] = 1
        queue.append((row, col))

        poppedRow, poppedCol = queue.popleft()
        board[poppedRow][poppedCol] = 0

        if result in sec_dir:
            if sec_dir[result] == 'D':
                dir_index = (dir_index + 1) % 4
            else:
                dir_index = (dir_index - 1) % 4

    if board[row][col] == 2:
        board[row][col] = 1
        queue.append((row, col))

        if result in sec_dir:
            if sec_dir[result] == 'D':
                dir_index = (dir_index + 1) % 4
            else:
                dir_index = (dir_index - 1) % 4

print(result)