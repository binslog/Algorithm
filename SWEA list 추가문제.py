# 13893. 주사위 굴리기











# --------------------------------------------------------
# 13748. 진기의 최고급 붕어빵
# T=int(input())
#
# for tc in range(1,T+1):
#     N,M,K = map(int,input().split())
#     members = list(map(int,input().split()))
#     members=sorted(members)
#
#     cnt=0
#     flag=0
#     for member in members:
#         if (member//M)*K  > cnt:
#             cnt+=1
#             flag=0
#         else:
#             flag=1
#             break
#
#     if flag:
#         print(f"#{tc} Impossible")
#     else:
#         print(f"#{tc} Possible")


# ---------------------------------------------------------
# 1979. 어디에 단어가 들어갈 수 있을까
# T=int(input())
#
# for tc in range(1,T+1):
#     N,M = map(int,(input().split()))
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     cnt=0
#     result = 0
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 cnt+=1
#             elif arr[i][j] == 0:
#                 if cnt == M :
#                     result +=1
#                     cnt=0
#                 else:
#                     cnt=0
#
#         if cnt==M:
#             result +=1
#             cnt=0
#         else:
#             cnt=0
#
#
#     for j in range(N):
#         for i in range(N):
#             if arr[i][j] == 1:
#                 cnt += 1
#             elif arr[i][j] == 0:
#                 if cnt == M:
#                     result += 1
#                     cnt = 0
#                 else:
#                     cnt = 0
#
#         if cnt==M:
#             result +=1
#             cnt=0
#         else:
#             cnt=0
#
#     print(f'{tc} {result}')
#

# ---------------------------------------------------------
# 1210. [S/W 문제 해결 기본] 2일차 - Ladder1
#
# for tc in range(1,11):
#     num=int(input())
#     ladder = [list(map(int,input().split())) for _ in range(100)]
#
#     directy = [0,0,-1] # 왼 오 위
#     directx = [-1,1,0]
#
#     # 역행해서 올라갈거야
#     def find_x(y,x):
#         while y:
#             for i in range(3):
#                 dy = directy[i] + y
#                 dx = directx[i] + x
#                 if dy > 99 or dy < 0 or dx > 99 or dx < 0 : continue
#                 if ladder[dy][dx] == 1:
#                     ladder[dy][dx] =3
#                     y += directy[i]
#                     x += directx[i]
#                     break
#         return dx
#
#     # '2'인 좌표 찾기
#     for i in range(100):
#         if ladder[99][i] == 2:
#             x=i
#             ret=find_x(99,x)
#
#     print(f'#{num} {ret}')

