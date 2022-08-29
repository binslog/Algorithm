# 금기륜 교수님 문제

# # A, B, C 를 만났을 때, H 를 X 로 변경해주는 함수
def change(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        # A일때는 1칸, B일때는 2칸, C일때는 3칸
        # 문자('C') - ord('A') = 2
        for j in range(1, ord(matrix[x][y]) - ord('A') + 2):
            new_x = x + (dx[i]*j)
            new_y = y + (dy[i]*j)
            # index 범위를 벗어나지 않는다면
            if 0 <= new_x < len(matrix) and 0 <= new_y <= len(matrix):
                # 원하는 범위에 있는 데이터가 H 라면 X 로 변경
                if matrix[new_x][new_y] == 'H':
                    matrix[new_x][new_y] = 'X'
#
#
#
# # T
T = int(input())
for test_case in range(1, T+1):
    # N
    N = int(input())
    # 2차원배열
    matrix = [list(input()) for _ in range(N)]

    # 2차원 배열을 탐색하면서
    for i in range(N):
        for j in range(N):
            # A or B or C 인가 ?
            # X 혹은 H 가 아니면 ? 으로도 구현할 수 있다
            if matrix[i][j] == 'A' or matrix[i][j] == 'B' or matrix[i][j] == 'C':
                change(i, j)
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         print(matrix[i][j], end='')
    #     print()

    # H 의 개수
    count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'H':
                count += 1
    print(f'#{test_case} {count}')
#

#---------------------------------------------------------------------------------------------------

# # 보충 수업 답안
# # 기지국에 영향을 받지 않는 집의 개수를 찾으시오.
#
# n = int(input())
# arr = [list(input()) for _ in range(n)]
#
# directy = [-1, 1, 0, 0]
# directx = [0, 0, -1, 1]
#
# len_dict = {'A': 1, 'B': 2, 'C': 3}
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 'X' or arr[i][j] == 'H':
#             continue
#         # K = 0
#         # if MAP[r][c] == 'A': K = 1
#         # elif MAP[r][c] == 'B': K = 2
#         # else: K = 3
#         m = len_dict[arr[i][j]]
#
#         for k in range(4):
#             for l in range(1, m + 1):
#                 dy = i + directy[k] * l
#                 dx = j + directx[k] * l
#                 if dy < 0 or dy >= n or dx < 0 or dx >= n:
#                     break
#                 if arr[dy][dx] == 'H':
#                     arr[dy][dx] = 'X'
#
# ans = 0
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 'H':
#             ans += 1
#
# print(ans)
# #
# # for line in arr:
# #     print(*line)
