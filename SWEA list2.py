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

# --------------------------------------------------------------

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
# 13700 이진탐색
# T=int(input())
# for tc in range(1,T+1):
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
#     # B 이진탐색
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

# ------------------------------------------------------------
# 13699. 색칠하기
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     arr2 = [[0]*10 for _ in range(10)]
#
#
#     for i in range(N):
#         if arr[i][4] == 1:
#             for k in range(arr[i][0],arr[i][2]+1):
#                 for l in range(arr[i][1],arr[i][3]+1):
#                     arr2[k][l] = 1
#
#
#     cnt=0
#     for i in range(N):
#         if arr[i][4] == 2:
#             for k in range(arr[i][0], arr[i][2] + 1):
#                 for l in range(arr[i][1], arr[i][3] + 1):
#                     if arr2[k][l] == 1:
#                         cnt +=1
#
#     print(f'#{tc} {cnt}')

# ------------------------------------------------------------
# 1208. [S/W 문제 해결 기본]1일차 - Flatten
# for tc in range(1,11):
#
#     N = int(input())
#     numbers = list(map(int,input().split()))
#
#     bucket = [0]*101 # bucket 만들고
#     for i in range(len(numbers)):
#         bucket[numbers[i]] +=1
#
#     while N:
#         if bucket[0] != 0 and bucket[-1] != 0:
#             bucket[-1] -=1
#             bucket[-2] +=1
#             bucket[0] -= 1
#             bucket[1] +=1
#             N -= 1
#
#         if bucket[0] == 0:
#             bucket = bucket[1:]
#         if bucket[-1] == 0:
#             bucket = bucket[0:-1]
#
#
#
#     result = len(bucket)-1
#     print(f'#{tc} {result}')










