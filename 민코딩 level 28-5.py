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
a,b = map(int,input().split())
arr = [[],
       [0,0,0,1,0,1,1],
       [0,1,0,0,1,0,0],
       [0,0,0,0,0,1,0],
       [0,1,0,0,0,0,0],
       [0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0]]

visited = [0]*7
answer=[]
def dfs(now):
    global answer
    print(now, end=" ")
    for i in range(7):
        if arr[now][i] == 1:
            dfs(i)




























# ------------------------------------------------------------------



# 2










