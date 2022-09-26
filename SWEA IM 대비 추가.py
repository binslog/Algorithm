# 6485. 삼성시의 버스노선
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     bus = [list(map(int,input().split())) for _ in range(N)]
#     P = int(input())
#     stops = [int(input()) for _ in range(P)]
#
#     result=[0]*P
#     for i in range(P):
#         for j in range(N):
#             if bus[j][0]<=stops[i]<=bus[j][1]:
#                 result[i] += 1
#
#     print(f'#{tc}',end=' ')
#     print(*result)

# ----------------------------------------------------------------------
# 5482. 쇠막대기 자르기







# -----------------------------------------------------------------------
# 2001. 파리 퇴치

# T = int(input())
#
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     X = N-M+1 # 파리채가 칠수 있는 범위
#
#
#     def flykill(y,x):
#         Sum=0
#         for i in range(M):
#             for j in range(M):
#                 dy = y+i
#                 dx = x+j
#                 Sum+=arr[dy][dx]
#         return Sum
#
#
#     Max = -21e8
#     for i in range(X):
#         for j in range(X):
#             ret=flykill(i,j)
#             if ret > Max:
#                 Max=ret
#
#
#     print(f'#{tc} {Max}')

# ---------------------------------------------
# 1974 스도쿠 검증
# T=int(input())
#
# for tc in range(1,T+1):
#     arr=[list(map(int,input().split())) for _ in range(9)]
#     flag=1
#
#     # 가로 검증
#     row_test = [[0] * 9 for _ in range(9)]
#     for i in range(9):
#         for j in range(9):
#             row_test[i][j]=arr[i][j]
#
#         if len(row_test[i]) != len(set(row_test[i])):
#             flag = 0
#             break
#
#     # 세로 검증
#     col_test = [[0] * 9 for _ in range(9)]
#     for j in range(9):
#         for i in range(9):
#             col_test[j][i]=arr[i][j]
#
#         if len(col_test[j]) != len(set(col_test[j])):
#             flag = 0
#             break
#
#     # 3*3 검증
#     last_test=[]
#     def find_sdc(y,x):
#         global flag, last_test
#         for k in range(3):
#             for l in range(3):
#                 dy=y+k
#                 dx=x+l
#                 last_test.append(arr[dy][dx])
#
#         if len(last_test) != len(set(last_test)):
#             flag = 0
#         else:
#             last_test = []
#
#         return flag
#
#
#     for i in range(0, 7, 3):
#         for j in range(0, 7, 3):
#             flag = find_sdc(i,j)
#
#
#     print(f'#{tc} {flag}')

# -----------------------------------------------------------------------









