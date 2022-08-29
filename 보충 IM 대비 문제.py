#11315 오목판정
# n = int(input())
# arr=[[0]*n for _ in range(n)]
#
# dr = [-1,-1,0,0]
# dc = [0,0,-1,1]
#
# diadr = [-1,-1,1,1]
# diadc = [-1,1,1,-1]
#
# r=c=3
# arr[r][c]='*'
# for i in range(4):
#     for j in range(1,n):
#         nr = r + dr[i]*j
#         nc = c + dc[i]*j
#         if nr < 0 or nr >= n or nc <0 or nr>=n: break
#
#         arr[nr][nc] = i+1
