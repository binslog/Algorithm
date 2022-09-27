n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

answer=[0]*3
def dfs(now,level):
    global answer
    answer[level]= now

    if level == 2:
        print(*answer)
        return

    for i in range(n):
        if arr[now][i]==1:
            dfs(i,level+1)

dfs(0,0)


