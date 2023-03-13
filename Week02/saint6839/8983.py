import sys

M, N, L = map(int, sys.stdin.readline().split())
shoot_pos = list(map(int,sys.stdin.readline().split()))
shoot_pos.sort()

animal_pos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
for a, b in animal_pos:
    lt = 0
    rt = len(shoot_pos) - 1
    forward_range = a + b - L
    behind_range = a - b + L

    while lt <= rt:
        mid = (lt + rt) // 2
        if forward_range <= shoot_pos[mid] <= behind_range:
            result += 1
            break
        elif forward_range > shoot_pos[mid]:
            lt = mid + 1
        elif behind_range < shoot_pos[mid]:
            rt = mid - 1

print(result)