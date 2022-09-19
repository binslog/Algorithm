# 1
# arr = [3,5,1,9,7]
# dir = [input() for _ in range(4)]
#
# for i in range(4):
#     if dir[i] == "R" :
#         x=arr[4]
#         for j in range(4,0,-1):
#             arr[j] = arr[j-1]
#         arr[0]=x
#
#     if dir[i] == "L" :
#         x=arr[4]
#         for j in range(4):
#             arr[j-1] = arr[j]
#         arr[3]=x
#
# print(*arr)

# ---------------------------------------------------
# 2
# arr = [[0,0,0,0],
#        [0,0,0,0],
#        [0,0,0,0]]
#
# dir = [list(map(int,input().split())) for _ in range(3)]
#
# flag=0
# for i in range(3):
#     y1,x1 = dir[0][0], dir[0][1]
#     y2,x2 = dir[1][0], dir[1][1]
#     y3,x3 = dir[2][0], dir[2][1]
#
# if y1==y2 or y2 == y3 or y1 == y3 :
#     flag = 1
# if x1==x2 or x2 == x3 or x1 == x3 :
#     flag = 1
#
# if flag:
#     print("위험")
# else:
#     print("안전")


# ------------------------------------------------------------
# 3
# arr = [[0,0,0,0],
#        [0,0,0,0],
#        [0,0,0,0],
#        [0,0,0,0]]
#
# nums = [list(map(int,input().split())) for _ in range(3)]
#
# for i in range(3):
#     for j in range(3):
#         arr[i][j]=nums[i][j] # 넣어주고
#
# for i in range(3):
#     for j in range(3):
#         arr[i][3] += arr[i][j] # row 합
#         arr[3][i] += arr[j][i] # column 합
#         if i ==j :
#             arr[3][3] += arr[i][j]
#
# for row in arr:
#     print(*row)

# ------------------------------------------------------------------
# 4
# arr = [[3,5,4,1],[1,1,2,3],[6,7,1,2]]
# nums = list(map(int,input().split()))
#
# for i in range(3):
#     for j in range(4):
#         if nums[0]==arr[i][j]:
#             arr[i][j]=nums[1]
#
#         elif nums[1]==arr[i][j]:
#             arr[i][j]=nums[2]
#
#         elif nums[2]==arr[i][j]:
#             arr[i][j]=nums[3]
#
#         elif nums[3]==arr[i][j]:
#             arr[i][j]=nums[0]
#
# for row in arr:
#     print(*row)

# --------------------------------------------------------------
# 5
# arr = list(map(int,input().split()))
# a=0
# b=7
#
# while True:
#     if a > b :
#         arr[0],arr[b] = arr[b],arr[0]
#         break
#
#     if arr[a] > arr[0] and arr[b] < arr[0] :
#         arr[a],arr[b] = arr[b],arr[a]
#
#     elif arr[a] <= arr[0]:
#         a+=1
#     elif arr[b] >= arr[0]:
#         b-=1
#
# print(*arr,sep=' ')

# -------------------------------------------------------
# 6
# arr1 = [["A","B","C","D"],
#         ["B","B","A","B"],
#         ["C","B","A","C"],
#         ["B","A","A","A"]]
#
# arr2 = [list(input()) for i in range(4)]
#
# check_dic ={"A":0,"B":0,"C":0,"D":0}
#
# for i in range(4):
#     for j in range(4):
#         if arr1[i][j] == arr2[i][j]:
#             check_dic[arr1[i][j]] += 1
#
# result_lst=[check_dic["A"],check_dic["B"],check_dic["C"],check_dic["D"]]
# result=max(result_lst)
#
# aa={i:j for j,i in check_dic.items()}
# print(aa.get(result))

