# 1
# arr=["A","B","C"]
# path=['']*5
#
# def abc(level):
#     if level ==2 :
#         for i in range(level):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(3):
#         path[level]=arr[i]
#         abc(level+1)
#         path[level]=0
#
# abc(0)

# ----------------------------------------------

# 2
# A,B,C = input(),input(),input()
# flag=0
#
# if A == B == C:
#     print("WOW")
#
# elif (A == B and A !=C) or (A!=B and B==C) or (A==C and B!=C):
#     print("GOOD")
#
# else: print("BAD")

# -----------------------------------------------------
# 3
# arr=["B","G","T","K"]
# path=['']*8
# depth=int(input())
#
# def abc(level):
#     if level == depth :
#         for i in range(level):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(4):
#         path[level]=arr[i]
#         abc(level+1)
#         path[level]=0
#
#
# abc(0)

# ---------------------------------------------------------
# 4
# arr = ["B5","B4","B3","B2","B1",1,2,3,4,5,6]
# idx = 5
# lst = [input() for _ in range(5)]
# print(lst)
#
# for i in range(len(lst)):
#     if lst[i] == "up" :
#         idx +=1
#     else:
#         idx -=1
#
# print(arr[idx])

# ------------------------------------------------------------
# 5
# br = int(input())
# path=['']*4
#
# def recur(depth):
#     if depth == 4:
#         print(*path,sep='')
#         return
#
#     for i in range(br):
#         path[depth]=i+1
#         recur(depth+1)
#
# recur(0)


# -------------------------------------------------------------
# 6
# arr = [input() for _ in range(4)]
# Max = -1
# Min = 10000
# Max_idx = 0
# Min_idx = 0
#
# for i in range(4):
#     if len(arr[i]) > Max:
#         Max = len(arr[i])
#         Max_idx = i
#
# for i in range(4):
#     if len(arr[i]) < Min:
#         Min = len(arr[i])
#         Min_idx = i
#
#
# print(f"긴문장:{Max_idx}\n짧은문장:{Min_idx}")

# --------------------------------------------------------------------
# 7
# arr = ["A","B","C","D"]
# path=['']*3
# target = list(input()) # 리스트로 받는다
# cnt =0
#
# def recursion(depth):
#     global cnt
#     if depth == 3:
#         # print(path)
#         if path == target:
#             print(f"{cnt+1}번째")
#         else:
#             cnt += 1
#         return
#
#     for i in range(4):
#         path[depth]=arr[i]
#         recursion(depth+1)
#
# recursion(0)

# -----------------------------------------------------------------------------
# 8
# arr1 = [[2,4],[1,5]]
# arr2 = [[2,3],[3,6]]
# arr3 = [[7,3],[1,5]]
#
# N = int(input())
# Max = -1
# Min = 10
#
# if N == 0:
#     for i in range(2):
#         for j in range(2):
#             if arr1[i][j] > Max:
#                 Max = arr1[i][j]
#
#             if arr1[i][j] < Min:
#                 Min = arr1[i][j]
#
# if N == 1:
#     for i in range(2):
#         for j in range(2):
#             if arr2[i][j] > Max:
#                 Max = arr2[i][j]

#             if arr2[i][j] < Min:
#                 Min = arr2[i][j]
#
# else:
#     for i in range(2):
#         for j in range(2):
#             if arr3[i][j] > Max:
#                 Max = arr3[i][j]
#
#             if arr3[i][j] < Min:
#                 Min = arr3[i][j]
#
# print(f'MAX={Max}\nMIN={Min}')

# ---------------------------------------------------------------------------
# 9
# passwords = ["JASON","Dr.tom","EXEXI","GK12P","POW"]
# A = input()
# flag=0
#
# for password in passwords:
#     if password.lower() == A.lower():
#         flag=1
#         break
#     flag=0
#
# if flag:
#     print("암호해제")
# else:
#     print("암호틀림")
#






