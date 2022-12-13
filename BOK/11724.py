from collections import deque
# collections 는 BFS를 위한 기본.

n,m,start=map(int,input().split()) # 노드, 간선 설정

A=[[] for _ in range(n+1)] # 간선을 만드는 빈 리스트를 만들어준다.

for _ in range(m):
    s,e=map(int,input().split())
    A[s].append(e)
    A[e].append(s) # 양방향 엣지이기 때문에 양쪽에 더한다.

for i in range(n+1):
    A[i].sort() # 번호가 작은 노드부터 정렬하기.

def DFS(v):
    print(v,end= ' ') # 하나씩 탐색
    visited[v] = True
    for i in A[v]:
        if not visited[i]: # 방문하지 않은 곳이면 DFS 들어간다..
            DFS(i)

visited=[False] * (n+1)
DFS(start)

def BFS(v):
    queue=deque() # 큐 하나 만들어준다.
    queue.append(v) # 더하고..!!
    visited2[v]=True
    while queue:
        now_Node = queue.popleft() # popleft를 사용한다...
        print(now_Node, end= ' ')
        for i in A[now_Node]:
            if not visited2[i]: #
                visited2[i] = True #
                queue.append(i)
print()
visited2 = [False] * (n+1)
BFS(start)


