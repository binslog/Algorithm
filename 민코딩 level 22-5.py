# 1
# arr =[[["A","T","B"],["C","C","B"]],[["A","A","A"],["B","B","C"]]]
# X = input()
# flag=0
#
# for i in range(2):
#     if flag: break
#     for j in range(2):
#         if flag: break
#         for k in range(3):
#             if arr[i][j][k] == X:
#                 flag=1
#                 break
#
#             else:
#                 flag=0
#
# if flag:
#     print("발견")
# else:
#     print("미발견")

# -------------------------------------------------------------
# 2
# arr = ['x','o']
#
# def abc(level):
#     if level == num:
#         for i in range(level):
#             print(path[i],end='')
#         print()
#         return
#     for i in range(2):
#         path[level]=arr[i]
#         abc(level+1)
#
# num=int(input())
# path=['']*num
# abc(0)

# -------------------------------------------------------------
# 3
# arr3=[[[0,0,0],[0,0,0],[0,0,0]],
#       [[0,0,0],[0,0,0],[0,0,0]],
#       [[0,0,0],[0,0,0],[0,0,0]]]
# X = input()
#
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             arr3[i][j][k] = chr(ord(X)+i)
#
# for row1 in arr3:
#     for row2 in row1:
#         print(*row2,sep='')
#     print()

# -----------------------------------------------------------
# 4
# arr3=[[[0,0,0],[0,0,0]],
#       [[0,0,0],[0,0,0]],
#       [[0,0,0],[0,0,0]]]
# a,b = map(int,(input().split()))
#
# for i in range(3):
#     for j in range(2):
#         for k in range(3):
#             arr3[i][0][k] = a
#             arr3[i][1][k] = b
#
# for row1 in arr3:
#     for row2 in row1:
#         print(*row2)
#     print()

# -----------------------------------------------------------
# 5
# MAP =[[3,5,4,2,2,3],[1,3,3,3,4,2],[5,4,4,2,3,5]]
# PRICE = ["T","P","G","K","C"]
#
# r,c = input().split()
# c = int(c)
#
# if r == "A":
#     r=0
# if r == "B":
#     r=1
# if r =="C":
#     r=2
#
# idx = MAP[r][c-1]
# print(PRICE[idx-1])

# --------------------------------------------------------
# 6
# arr = [list(input()) for _ in range(4)]
#
# for i in range(len(arr)-1):
#     for j in range(i+1,len(a)):
#         if len(arr[i]) > len(arr[j]) :
#             arr[i],arr[j]=arr[j],arr[i]
#
# for row in arr:
#     print(*row,sep='')
#

# --------------------------------------------------
# 8
# arr3=[[[" ","#"," "],["#"," ","#"],["#","#","#"],["#"," ","#"],["#"," ","#"]],
#      [["#","#","#"],["#"," ","#"],["#","#","#"],["#"," ","#"],["#","#","#"]],
#      [["#","#","#"],["#"," ","#"],["#"," "," "],["#"," ","#"],["#","#","#"]],
#      [["#","#"," "],["#"," ","#"],["#"," ","#"],["#"," ","#"],["#","#"," "]]]
#
# idx = int(input())
# result=arr3[idx]
#
# for row in result:
#     print(*row,sep='')














