# 1
# arr = ['시작',3,1,2,1,3,2,1,2,1,'도착']
#
# def dfs(now):
#     if now == len(arr)-1:
#         print(arr[now],end=' ')
#         return
#
#     print(arr[now],end=' ')
#     dfs(now+arr[now])
#     print(arr[now],end=' ')
#
# n=int(input())
# print("시작",end=' ')
# dfs(n)
# print("시작")

# ------------------------------------------
# 2
# evid = [-1,0,0,1,2,4,4]
# times = [8,3,5,6,8,9,10]
#
# def dfs(now):
#     if now == 0:
#         print(f'{now}번index(출발)')
#         return
#
#     dfs(evid[now])
#     print(f'{now}번index({times[now]}시)')
#
# n=int(input())
# dfs(n)


# ----------------------------------------
# 3
# arr = [list(map(int,input().split())) for _ in range(3)]
#
# for i in range(3):
#     if len(set(arr[i])) == 1:
#         print(arr[i][0])
#     else:
#         print("x")

# ------------------------------------------
# 4
# arr1 = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))
#
# result=[]
# for i in range(4):
#     if arr1[i]< arr2[i]:
#         result.append(arr1[i])
#         result.append(arr2[i])
#     else:
#         result.append(arr2[i])
#         result.append(arr1[i])
#
# print(*result)

# ---------------------------------------------
# 5
# arr = [list(map(int,input().split())) for _ in range(4)]
# visited = [list(map(int,input().split())) for _ in range(4)]
# y1,x1=0,0
# y2,x2=0,0
#
# dy=[-1,1,0,0]
# dx=[0,0,-1,1]
#
# ny,nx=0,0
#
# def find_1(y,x):
#     global ny,nx
#     for i in range(4):
#         y+= dy[i]
#         x+= dx[i]
#         if y<0 or y>4 or x<0 or y>4: continue
#         if arr[y][x] == 0 : continue
#         if arr[y][x] ==1 and visited[y][x]==0:
#             visited[ny][nx]=1
#             continue
#         if ny
#
#
#
# for i in range(4):
#     for j in range(5):
#         if arr[i][j] == 1:
#             visited[i][j] =1
#             y1,x1=i,j
#             ret=find_1(i,j)
#
# print('(%d,%d)' % (y1,x1))
# print('(%d,%d)' % (y2,x1))

# -------------------------------------------------------
# 6
# arr = [[3,2,5,3],[7,6,1,6],[4,9,2,7]]
# rot = list(map(int,input().split()))
#
# for i in range(3):
#     num=rot[i]%3
#     ni=0
#     for j in range(4):
#         ni+=i+num
#         arr[j][i]=arr[j][ni]
#
# print(*arr,sep='')

# --------------------------------------------------------
# 7
# a,b = map(int,input().split())
# swam = [0,0,0,0,0]



# -----------------------------------------------------
# 8





# ------------------------------------------------------------
# 9























