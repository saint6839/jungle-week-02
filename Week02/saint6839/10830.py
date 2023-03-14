import sys
sys.setrecursionlimit(10**6)
N, B = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def get_remain(m):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] += m[i][j] % 1000
    return temp

def mul_matrix(m1, m2):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += m1[i][k] * m2[k][j] % 1000
    return temp

def dac(m, b):
    if b == 1:
        return get_remain(m)

    temp = dac(m, b//2)

    if b % 2 == 0:
        return mul_matrix(temp, temp)
    else:
        return mul_matrix(mul_matrix(temp, temp), m)

for i in range(N):
    print(*get_remain(dac(matrix, B))[i])