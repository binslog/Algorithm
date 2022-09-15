N,M,L = map(int,(input().split()))
arr = [list(map(int,input().split())) for _ in range(M)]
tree = [0]*(N+1)
# print(N,M,L)
# print(arr)

for i in range(M):
    idx,num=map(int,input().split())
    tree[idx] = num

for i in range(N,L-1,-1):
    if
