name=['A','B','C','D','E']
st=input()
arr=[
    [0,1,0,0,0],
    [0,0,1,1,1],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [0,0,0,0,0],
]
used=[0]*5
cnt=0
def dfs(now):
    global cnt
    if name[now]=='E':
        cnt+=1
    for i in range(5):
        if arr[now][i]==1 and used[i]==0:
            used[i]=1
            dfs(i)
            used[i]=0

st_index=0
for i in range(5):
    if name[i]==st:
        st_index=i
        break
used[st_index]=1
dfs(st_index)
print(cnt)

arr = [[0,0,0,0,0,0,0],
       [0,0,0,1,0,1,1],
       [0,1,0,0,1,0,0],
       [0,0,0,0,0,1,0],
       [0,1,0,0,0,0,0],
       [0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0]]