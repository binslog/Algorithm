# 1
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# def dfs(now):
#     print(now, end=' ')
#     for i in range(N):
#         if arr[now][i] == 1:
#             dfs(i)
# dfs(0)

# ---------------------------------------------------
# 2
# st,ed = map(int,input().split())
# # 인덱스를 +1 하려고 배열을 하나 더 만들어 줄거야
# # 배열 만들 필요 없이 하기 위함, 1번 인덱스는 1, 6번 인덱스는 6...
#
# arr = [[0,0,0,0,0,0,0],
#        [0,0,0,1,0,1,1],
#        [0,1,0,0,1,0,0],
#        [0,0,0,0,0,1,0],
#        [0,1,0,0,0,0,0],
#        [0,1,0,0,0,0,0],
#        [0,0,0,0,0,0,0]]
#
# visited = [0]*7 # 싸이클을 없애기 위해서
# cnt=0
# result=0
# def dfs(now):
#     global cnt,result
#     if now == ed: # 현재 깊이가 목적지와 같은 순간
#         result=cnt
#         return
#
#     for i in range(7): # 배열 돌아서
#         if arr[now][i] == 1 and visited[i]==0:
#             visited[i]=1
#             cnt+=1
#             dfs(i)
#             visited[i]=0
#             cnt-=1
#
#
# visited[st]=1
# dfs(st)
#
# print(result)























# ------------------------------------------------------------------



# 2










