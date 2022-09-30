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

# arr = ['시작',3,1,2,1,3,2,1,2,1,'도착']
#
# def dfs(now):
#     if now == len(arr)-1:
#         print(arr[now],end=' ')
#         return
#
#     print(arr[now],end=' ')
#     if now == 0:
#         dfs(n)
#     else:
#         dfs(now+arr[now])
#     print(arr[now],end=' ')
#
# n=int(input())
# dfs(0)

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
#
# # 아래쪽, 오른쪽
# dy=[1,0]
# dx=[0,1]
#
# def find_1(y,x):
#     dir=0
#     while True:
#         y+= dy[dir]
#         x+= dx[dir]
#         if y<0 or y>4 or x<0 or y>4 or arr[y][x] == 0:
#             y -= dy[dir]
#             x -= dx[dir]
#             dir = (dir+1)%2
#
#         elif x==4 : break
#         elif arr[y+dy[0]][x+dx[0]]==0 and arr[y+dy[1]][x+dx[1]] ==0: break
#
#     return y,x
#
#
#
# y1,x1=0,0
# y2,x2=0,0
# flag=0
# for i in range(4):
#     if flag:
#         break
#     for j in range(5):
#         if arr[i][j] == 1:
#             flag=1
#             y1,x1 = i,j
#             y2,x2 = find_1(y1, x1)
#             print('(%d,%d)' % (y1, x1))
#             print('(%d,%d)' % (y2, x2))
#             break


# -------------------------------------------------------
# 6
# arr = [[3,2,5,3],[7,6,1,6],[4,9,2,7]]
# rot = list(map(int,input().split()))
# result=[[0]*4 for _ in range(3)]
#
# for i in range(4):
#     if rot[i] % 3 == 1:
#         result[1][i] = arr[0][i]
#         result[2][i] = arr[1][i]
#         result[0][i] = arr[2][i]
#
#     elif rot[i] % 3 == 2:
#         result[2][i] = arr[0][i]
#         result[1][i] = arr[2][i]
#         result[0][i] = arr[1][i]
#     else:
#         result[i]=arr[i]
#
#
# for row in result:
#     print(*row,sep='')


# --------------------------------------------------------
# 7
# idx,life = map(int,input().split())
# road = [["_"]*5 for _ in range(life+1)]
#
# for i in range(life,0,-1):
#     for j in range(5):
#         if j-life == life:
#             road[life-i][j-i]=i
#             break
#
# for row in road:
#     print(*row,sep='')


# -----------------------------------------------------
# 8
# MAP=[list(input().split()) for _ in range(4)]
#
# directy = [0,1,0,-1,0]
# directx = [1,0,-1,0,1]
#
# ny,nx,dir=0,0,0
# def monster(y,x):
#     global ny,nx,dir
#     while dir !=5:
#         y += directy[dir]
#         x += directx[dir]
#         if y<0 or y>=4 or x<0 or x>=3 or MAP[y][x] =="#" or MAP[y][x]!="_":
#             y -= directy[dir]
#             x -= directx[dir]
#             dir +=1
#         else:
#             dir +=1
#
#     MAP[ny][nx]=MAP[y][x]
#
# for i in range(4):
#     for j in range(3):
#         if MAP[i][j] != "#" or MAP[i][j] != "_":
#             monster(i,j)
#
# print(MAP)


# ------------------------------------------------------------
# 9
# word1=list(input())
# word2=list(input())
#
# lst1=[]
# for i in range(len(word1)):
#     for j in range(i+1,len(word1)):
#         lst1.append(word1[i:j+1])
#
# lst2=[]
# for i in range(len(word2)):
#     for j in range(i+1,len(word2)):
#         lst2.append(word2[i:j+1])
#
# result=[]
# for i in range(len(lst1)):
#     for j in range(len(lst2)):
#         if lst1[i] == lst2[j] :
#             result.append(lst2[j])
#
#
# Max=-21e8
# idx=0
# for i in range(len(result)):
#     if len(result[i]) >Max:
#         Max=len(result[i])
#         idx=i
#
# print(*result[idx],sep='')
