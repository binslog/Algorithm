#1945 간단한 소인수분해

# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     a, b, c, d, e = 0, 0, 0, 0, 0
#     while N%2==0:
#         N = N / 2
#         a += 1
#
#     while N%3==0:
#         N = N / 3
#         b += 1
#
#     while N%5==0:
#         N = N / 5
#         c += 1
#
#     while N%7==0:
#         N = N / 7
#         d += 1
#
#     while N%11==0:
#         N = N / 11
#         e += 1
#
#     print(f'#{tc} {a} {b} {c} {d} {e}')


# ------------------------------------------------------------
# 1974 스도쿠 검증

# T=int(input())
#
# for tc in range(1,T+1):
#     arr = [list(map(int,input().split())) for i in range(9)]
#
#     # row test
#     row_flag = 1
#     for i in range(9):
#         if len(set(arr[i])) != 9:
#             row_flag=0
#             break
#
#     # column test
#     col_flag = 1
#     col_lst=[[0]*9 for i in range(9)]
#     for i in range(9):
#         for j in range(9):
#             col_lst[i][j]=arr[j][i]
#
#     for i in range(9):
#         if len(set(col_lst[i])) != 9:
#             col_flag=0
#             break
#
#     # block test
#
#     def block_func(y,x):
#         block_flag = 1
#         blk_lst = []
#         for i in range(3):
#             for j in range(3):
#                 blk_lst.append(arr[i+y][j+x])
#
#         if len(set(blk_lst)) != 9:
#             return 0
#         else:
#             return 1
#
#     for i in range(0,9,3):
#         for j in range(0,9,3):
#             block_flag=block_func(i,j)
#
#     result = 0
#     if row_flag == 1 and col_flag ==1 and block_flag ==1 :
#         result = 1
#     else:
#         result = 0
#
#
#     print(f'#{tc} {result}')


# -------------------------------------------------------------------------------------

# 2001 파리 퇴치

# T = int(input())
#
# for tc in range(1,T+1):
#     n, m = map(int, (input().split()))
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     Max = -21e8
#     result = []
#     for i in range(n-m+1):
#         for j in range(n-m+1):
#             tmp = 0
#             for k in range(m):
#                 tmp += sum(arr[i+k][j:j+m])
#
#             if Max < tmp:
#                 Max = tmp
#
#     print(f'#{tc} {Max}')

# ---------------------------------------------------------------------------
# 삼성시의 버스노선
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     station = [list(map(int,input().split())) for _ in range(N)]
#     bus_num = int(input())
#     bus= [int(input()) for _ in range(bus_num)]
#
#
#     counts = [0] * bus_num
#     for i in range(N):
#         for j in range(bus_num):
#             if station[i][0] <= bus[j] and bus[j] <= station[i][1]:
#                 counts[j] += 1
#
#     result = ' '.join(map(str,counts))
#     print(f'#{tc} {result}')









