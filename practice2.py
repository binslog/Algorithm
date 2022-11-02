T=int(input())

for tc in range(1,1+T):
    n=int(input())
    arr=[list(map(int,input())) for _ in range(n)]

    visited = [[0]*n for _ in range(n)]
    flag=0
    directy = [-1, 0, 0]
    directx = [0, -1, 1]


    def dfs(y,x):
        global flag
        if arr[y][x] == 3:
            flag=1
            return

        for i in range(3):
             dy=y+directy[i]
             dx=x+directx[i]
             if dy<0 or dx<0 or dy>=n or dx>=n: continue  # 배열범위 벗어나면 안됨
             if visited[dy][dx]==1: continue              # 이미 방문했던 곳이면 안됨
             if arr[dy][dx]==1: continue                # 벽이면 못감

             else:
                visited[dy][dx]=1
                dfs(dy,dx)
                visited[dy][dx]=0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                visited[i][j]=1
                dfs(i,j)    #y,x 좌표값

    print(f'#{tc} {flag}')