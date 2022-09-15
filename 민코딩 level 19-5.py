#2
# arr = [list(map(int,input().split())) for _ in range(5)]
#
# directy=[-1, -1, -1, 0, 0, 1, 1, 1]
# directx=[-1, 0, 1, -1, 1, -1, 0, 1]
#
#
# def cell(y,x):
#     flag = 0
#     for i in range(8):
#         dy = directy[i] + y
#         dx = directx[i] + x
#
#         if dy < 0 or dy > 4 or dx < 0 or dx > 3 : continue
#
#         if arr[dy][dx] != 0:
#             flag = 1
#             break
#         else:
#             flag = 0
#
#     return flag
#
#
# ret=[]
# for i in range(5):
#     for j in range(4):
#         ret = cell(i,j)
#
#
# if ret == 1:
#     print("불안정한 상태")
# else:
#     print("안정된 상태")

#----------------------------------------------------------------------------
#3
# nums = list(map(int,input().split()))
# arr = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
#
# for i in range(len(nums)):
#     y = nums[i]//4
#     if nums[i] % 4 == 0:
#         y -=1
#     x = nums[i]%4 -1
#     idx = i
#     arr[y][x] = i+1
#
# for row in arr:
#     print(*row)

#-----------------------------------------------------------------
#4
# arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# lst = [input().split() for i in range(3)]
#
# for i in range(3):
#     lst[i][1] = int(lst[i][1])
# # [['G', 3], ['S', 2], ['S', 0]]
#
# for i in range(3):
#     if lst[i][0] == "G":
#         for j in range(4):
#             arr[lst[i][1]][j] = 1
#
#     if lst[i][0] == "S":
#         for j in range(4):
#             arr[j][lst[i][1]] = 1
#
# for row in arr:
#     print(*row)

#----------------------------------------------------------------------
#6
# arr = [["A","B","G","K"],["T","T","A","B"],["A","C","C","D"]]
# pat = [list(input()) for _ in range(2)]
#
# def ispattern(y,x):
#     for i in range(2):
#         for j in range(2):
#             dy = y+i
#             dx = x+j
#             if pat[i][j] == arr[dy][dx]:
#                 return 1
#         return 0
#
#
# for i in range(2):
#     for j in range(3):
#         ret = ispattern(i,j)
#
# if ret==1:
#     print(f'발견({ret}개)')
# else:
#     print("미발견")

#--------------------------------------------------------------------------------
#7
arr=[[3,5,1],[3,8,1],[1,1,5]]
bit_arr = [list(map(int,input().split())) for _ in range(2)]

def ispattern(y,x):
    Sum = 0
    for i in range(2):
        for j in range(2):
            if bit_arr[i][j] == 1:
                dy = y+i
                dx = x+j
                Sum += arr[dy][dx]
    return Sum

Max = -1
for i in range(2):
    for j in range(2):
        ret = ispattern(i,j)
        if ret > Max:
            Max = ret
            y=i
            x=j

print("(%d,%d)"% (y,x))



































