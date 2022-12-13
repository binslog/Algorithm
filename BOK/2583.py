from collections import deque
# bfs를 하기 위한 첫 번째

def BFS(i,j):
    queue = deque() # 큐를 deque()으로 만들어준다.
    queue.append((i,j)) # 들어가는 자리를
    d=[(-1,0),(0,-1),(1,0),(0,1)] # 좌표를 상하좌우로 델타탐색 한다.
    cnt=1 # 들어갈 때 cnt 하나 해준다.

    while queue: # 큐가 빌 때 까지 해준다.
        y,x = queue.popleft() # 맨 왼쪽 값 뽑고 리스트에서 삭제
        for dy,dx in d : # for _ in range(4) 델타 탐색 상하좌우 하는 느낌으로
            Y,X = y+dy, x+dx # 델타 탐색 해주고,
            if (0<= Y < M) and (0 <= X < N) and graph[Y][X] == 0: # 범위 안에 있거나, 가보지 않았으면
                graph[Y][X] = 1 # 1 넣어주고
                queue.append((Y,X)) # 해당 좌표 넣어주고
                cnt +=1 # 1 더해주고..

    return cnt # 끝나면 count한 값

M,N,K = map(int,input().split())
graph = [[0]*N for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0: # 공백이면,
            graph[i][j] = 1 # 1을 칠해주고
            result.append(BFS(i,j)) # bfs 돌아준다.


print(len(result))
print(*sorted(result))


