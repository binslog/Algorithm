# 2210 숫자판 점프

directy=[1,-1,0,0]
directx=[0,0,1,-1]
result=[]

lst=[]
def DFS(y,x):
    global lst
    if len(lst) == 6: # [[1,1,1,1,1,1], [1,2,3,3,3,3],[....]
        if lst not in result: # 개수가 6개가 되면 끝낸다.
            result.append(lst) # 정답 리스트에 추가해준다

        lst = []
        return

    for i in range(4):
        dy=y+directy[i]
        dx=x+directx[i]
        if 0<=dy<5 and 0<=dx<5:
            lst.append(arr[dy][dx])
            DFS(dy,dx)


arr = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        DFS(i,j)

print(len(result))
