T=int(input())

for tc in range(1,1+T):
    v,e = map(int,input().split())
    arr = [[] for _ in range(100)]
    for _ in range(e):
        st, ed = map(int,input().split())
        arr[st].append(ed)
    start,end= map(int,input().split())
    result=0
    used=[0]*(v+1)

    def dfs(now):
        global result
        if now == end:
            result=1
            return

        for i in range(len(arr[now])):
            if used[now] == 0:
                used[now]=1
                dfs(arr[now][i])
                used[now]=0

    dfs(start)
    print(f'#{tc} {result}')

