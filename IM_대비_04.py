# 5789. 현주의 상자 바꾸기

# T = int(input())
#
# for tc in range(1,T+1):
#     N,Q = map(int,input().split())
#     box = [0]*N
#     arr = [list(map(int,input().split())) for _ in range(Q)]
#
#     for i in range(Q):
#         for j in range(arr[i][0]-1,arr[i][1]):
#             box[j] = i+1
#
#     print(f'#{tc}',end=' ')
#     print(*box)

# --------------------------------------------------
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

# ----------------------------------------------------------------
# 1204 .[S/W 문제해결 기본] 1일차 - 최빈수 구하기
#
# T=int(input())
#
# for tc in range(1,1+T):
#     num=int(input())
#     scores = list(map(int,input().split()))
#     bucket = [0]*1001
#     result=0
#
#     for i in range(len(scores)):
#         bucket[scores[i]] +=1 # DAT 만들어주고,
#
#     for i in range(len(bucket)):
#         if bucket[i] == max(bucket):
#             result=i
#
#
#     print(f'#{num} {result}')

# ----------------------------------------------------------------
# 12712. 파리퇴치3

# T=int(input())
# for tc in range(1,T+1):
#     n,m=map(int,input().split())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#
#     # + 방향으로 가기 위한 조작
#     direct1_y=[-1,1,0,0]
#     direct1_x=[0,0,-1,1]
#
#     # x 방향으로 가기 위한 조작
#     direct2_y=[-1,-1,1,1]
#     direct2_x=[-1,1,-1,1]
#
#     def fly(y,x):
#         # + 방향 sum 출력
#         Sum1=0
#         for i in range(1,m):
#             for j in range(4):
#                 dy=direct1_y[j]*i+y
#                 dx=direct1_x[j]*i+x
#                 if dy<0 or dy>=n or dx<0 or dx>=n: continue
#                 Sum1+=arr[dy][dx]
#
#         # x 방향 sum 출력
#         Sum2=0
#         for i in range(1,m):
#             for j in range(4):
#                 dy=direct2_y[j]*i+y
#                 dx=direct2_x[j]*i+x
#                 if dy < 0 or dy >= n or dx < 0 or dx >= n: continue
#                 Sum2+=arr[dy][dx]
#
#         result = 0
#         if Sum1>Sum2:
#             return Sum1+arr[y][x] # 이거 중요한데, 본인까지 퇴치 해야한다.
#         else:
#             return Sum2+arr[y][x]
#
#
#     # 출력한 값에 Max를 구해야한다.
#     Max=-1000
#     for i in range(n):
#         for j in range(n):
#             ret=fly(i,j)
#             if ret > Max:
#                 Max = ret
#
#     print(f'{tc} {Max}')

# ------------------------------------------------------------------------------

# 1954. 달팽이 숫자

# T=int(input())
# for tc in range(1,1+T):
#     n=int(input())
#     arr=[[0]*n for _ in range(n)]
#
#     directy = [0,1,0,-1]
#     directx = [1,0,-1,0]
#
#     dy,dx=0,0
#     dir=0
#
#     for i in range(1,n*n+1):
#         arr[dy][dx] += i
#         dy += directy[dir]
#         dx += directx[dir]
#
#         if 0>dy or dy>=n or dx<0 or dx>=n or arr[dy][dx]!=0 :
#             dy-=directy[dir]
#             dx-=directx[dir]
#
#             dir = (dir+1)%4
#
#             dy+=directy[dir]
#             dx+=directx[dir]
#
#
#     print(f'#{tc}')
#     for row in arr:
#         print(*row)
#

# ----------------------------------------------------------------
# 11315. 오목판정

# T=int(input())
#
# for tc in range(1,T+1):
#     n = int(input())
#     arr = [list(input()) for _ in range(n)]
#
#     # 아래, 오른쪽, 대각선 아래를 향한 방향 설정
#     directy = [1,0,1,1]
#     directx = [0,1,1,-1]
#
#     def omok(y,x):
#         flag = 0
#         for i in range(4):   # 델타배열 돌면서
#             cnt = 0  # 함수가 올 때 마다 초기화
#             for j in range(1,5):  # 5개만 맞으면 오목임! 근데 이미 2개 있으니까
#                 dy=directy[i]*j+y  # 새로운 y
#                 dx=directx[i]*j+x  # 새로운 x
#                 if not (0<= dx < n and 0<= dy < n): continue
#                 if arr[dy][dx] == "o": # 또 o가 있으면!
#                     cnt += 1
#
#             if cnt >= 4:
#                 flag = 1
#                 break
#
#         return flag
#
#     # print(omok(0, 4))
#     ret_flag = 0
#     for i in range(n):
#         for j in range(n): #
#             if arr[i][j] == "o":
#                 ret = omok(i,j)
#
#                 if ret:
#                     ret_flag = 1
#                     break
#
#         if ret_flag == 1:
#             break
#
#
#     if ret_flag==1:
#         print(f'#{tc} YES')
#     else:
#         print(f'#{tc} NO')
#


# ----------------------------------------------------------------

# 1860. 진기의 최고급 붕어빵




#-----------------
# 6190. 정곤이의 단조 증가하는 수

# T=int(input())
#
# for tc in range(1,1+T):
#     n=int(input())
#     numbers=list(map(int,input().split()))
#
#     X=0 # 곱한 값
#     flag=0
#
#     result=[]
#     for i in range(n):
#         for j in range(i+1,n):
#             X=list(str(numbers[i]*numbers[j]))
#             Y=int(numbers[i]*numbers[j])
#
#
#             for k in range(len(X)-1):
#                 if X[k] > X[k+1]:
#                     flag=0
#                     break
#                 else: flag=1
#
#             if flag:
#                 result.append(Y)
#
#
#     if len(result)==0:
#         print(f'#{tc} -1')
#     else:
#         print(f'#{tc} {max(result)}')




