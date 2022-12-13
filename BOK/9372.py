# 9372 상근이의 여행
# DFS 기본.

T=int(input())
for tc in range(1,1+T):

    n,m = map(int,input().split()) # 국가의 수가 노드, 비행기를 간선의 수라고 생각.
    lst=[[] for _ in range(n+1)] # 빈 리스트를 만들어준다.

    for _ in range(m):
        x,y = map(int, input().split())
        lst[x].append(y)
        lst[y].append(x) # 양방향으로 해주는 것이 포인트

    cnt=0
    def DFS(now):
        global cnt
        visited[now]=True
        cnt+=1  # 하나 지날때마다 cnt 해준다.

        for i in lst[now]: # 1부터 시작!
            if not visited[i]: # false이면..
                DFS(i)


    visited = [False] * (n+1) # 하나 크게 설정
    DFS(1) # 국가는 무조건 1부터 시작한다.
    result=cnt-1 # 처음 들어 갈 때 카운트 빼주면 비행기(간선)의 최소값이 나온다.
    print(result)
