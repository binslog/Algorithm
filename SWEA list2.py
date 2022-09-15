# 13704 달팽이 숫자

# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [[0]*N for _ in range(N)]
#
#     directy = [0,1,0,-1]
#     directx = [1,0,-1,0]
#     y,x= 0,0
#     dir=0
#
#     for i in range(1,N*N+1):
#         arr[y][x] += i
#         y += directy[dir]
#         x += directx[dir]
#
#         if y<0 or x<0 or y>=N or x>=N or arr[y][x] != 0:
#             y-=directy[dir]
#             x-=directx[dir]
#
#             dir = (dir+1) % 4
#
#             y += directy[dir]
#             x += directx[dir]
#
#     print(f'#{tc}')
#     for row in arr:
#         print(*row)

#--------------------------------------------------------------
# 13702 델타검색
# for tc in range(1,11):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     directy = [-1,1,0,0]
#     directx = [0,0,-1,1]
#
#     def ptnsum(y,x):
#         Sum = 0
#         for i in range(4):
#             dy = directy[i]+y
#             dx = directx[i]+x
#             if dy<0 or dx<0 or dx>N-1 or dy>N-1: continue
#             Sum += abs(arr[dy][dx]-arr[y][x])
#         return Sum
#
#     result = 0
#     for i in range(N):
#         for j in range(N):
#             rtn = ptnsum(i,j)
#             result += rtn
#
#     print(f'#{tc} {result}')

#------------------------------------------------------

# T=int(input())
# for tc in range(1,T+1):
#     # 이진탐색
#     end,targetA,targetB=map(int,(input().split()))
#     endA=end
#     startA=0
#     cntA=0
#
#     # A 이진탐색
#     while startA<=endA:
#         mid=(startA+endA)//2
#         cntA += 1
#         if mid == targetA:
#             break
#         elif mid < targetA:
#             startA=mid
#         else:
#             endA=mid
#
#     endB=end
#     startB=0
#     cntB=0
#     while startB<=endB:
#         mid=(startB+endB)//2
#         cntB += 1
#         if mid == targetB:
#             break
#         elif mid < targetB:
#             startB=mid
#         else:
#             endB=mid
#
#     if cntA>cntB:
#         print(f'#{tc} B')
#     elif cntA<cntB:
#         print(f'#{tc} A')
#     else:
#         print(f'#{tc} 0')

#------------------------------------------------------------
# 색칠하기
N = int(input())






