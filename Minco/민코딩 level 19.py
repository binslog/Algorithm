#1
# arr = [[3,5,4],[1,1,2],[1,3,9]]
# y,x = map(int,(input().split()))
#
# directy = [-1,1,0,0]
# directx = [0,0,-1,1]
#
# sum = 0
# for i in range(4):
#     dy = directy[i] + y
#     dx = directx[i] + x
#     if dy < 0 or dy > 3 or dx < 0 or dx > 3: continue
#
#     sum += arr[dy][dx]
#
# print(sum)

#-------------------------------------------------------------------------------
#2
# arr = [[3,3,5,3,1],[2,2,4,2,6],[4,9,2,3,4],[1,1,1,1,1],[3,3,5,9,2]]
# directy = [-1, 1, -1, 1]
# directx = [-1, -1, 1, 1]
# Max = -100000
#
# Maxy = 0
# Maxx = 0
#
# def diagonal(y,x):
#     Sum = 0
#     for i in range(4):
#         dy = directy[i] + y
#         dx = directx[i] + x
#         if dy < 0 or dy > 4 or dx < 0 or dx > 4: continue
#         Sum += arr[dy][dx]
#     return Sum
#
# for i in range(5):
#     for j in range(5):
#         ret = diagonal(i,j)
#         if ret > Max:
#             Max = ret
#             Maxx=i
#             Maxy=j
#
# print(Maxx,Maxy)


#--------------------------------------------------------------------------------
#3
# boom = [['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_']]
# lst = [list(map(int,input().split())) for i in range(2)]
# # print(lst)
#
#
# def booming(y,x):
#     directy = [-1, -1, -1, 0, 0, 1, 1, 1]
#     directx = [-1, 0, 1, -1, 1, -1, 0, 1]
#     for j in range(8):
#         dy = directy[j] + y
#         dx = directx[j] + x
#
#         if dy < 0 or dy > 3 or dx < 0 or dx >4 : continue
#         boom[dy][dx]="#"
#
#     return boom
#
#
# for i in range(2):
#     y, x = lst[i][0],lst[i][1]
#     ret = booming(y, x)
#
# for row in ret:
#     print(*row)

#-----------------------------------------------------------------------------------------
#7
# matrix = [list(map(int,input().split())) for _ in range(4)]
# vect =[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
#
# idx = []
# for i in range(4):
#     vect[matrix[i][0]][matrix[i][1]] = 5
#
# for row in vect:
#     print(*row)


#--------------------,-------------------
#8
# arr = [list(map(int,input().split())) for _ in range(4)]
#
# directy = [0,0,0,1,1,1]
# directx = [0,1,2,0,1,2]
#
# Max =-1
# Maxy=0
# Maxx=0
#
# def rectSum(y,x):
#     Sum = 0
#     for i in range(6):
#         dy = directy[i] + y
#         dx = directx[i] + x
#         if dy > 3 or dy < 0 or dx > 3 or dx < 0 : continue
#
#         Sum += arr[dy][dx]
#
#     return Sum
#
# for i in range(3):
#     for j in range(2):
#         ret = rectSum(i,j)
#         if ret > Max :
#             Max = ret
#             Maxy = i
#             Maxx = j
#
# print(f"({Maxy},{Maxx})")




