# 1
# name = ["Amy","Edger","Bob","Diane","Chloe"]
#
# arr = [[0,1,0,0,0],
#        [0,0,0,0,0],
#        [1,0,0,0,0],
#        [0,0,1,0,0],
#        [0,0,1,0,0]]
#
# sum = 0
# max = 0
# maxindex = 0
#
#
# for j in range(5):
#     sum=0
#     for i in range(5):
#         if arr[i][j] == 1:
#             sum += 1
#
#         if sum > max :
#             max = sum
#             maxindex =j
#
# print(name[maxindex])

# -----------------------------------------------------------
# 2
# num = int(input())
# arr = [list(map(int,input().split())) for _ in range(num)]
#
# boss_index = []
# under_index = []
#
# for i in range(num):
#     if arr[i][0] == 1:
#         boss_index.append(i)
#
# boss_index = ' '.join(str(s) for s in boss_index)
# print(f'boss:{boss_index}')
#
#
# def dfs(now):
#     for k in range(num):
#         if arr[now][k] == 1 :
#             under_index.append(k)
#             dfs(k)
# dfs(0)
#
# under_result = ' '.join(str(s) for s in under_index)
# print(f"under:{under_result}")

# ------------------------------------------------------------------------
# # 3
# arr = [[0,1,1,0,0,0,0,1],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,1,1,0,1,0],
#        [0,0,0,0,0,1,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0]]
#
#
# def dfs(now):
#     for i in range(8):
#         if arr[i][now] == 1:
#             y=i
#         else: return 1
#
#     result=[]
#     for j in range(8):
#         if arr[y][j] == 1 and arr2[j] != X:
#             result.append(arr2[j])
#
#     return result
#
#
# X=input()
# arr2=["A","B","C","D","E","F","G","H"] # 받아온 알파벳을 인덱스로 바꾸어준다.
# for i in range(8):
#     if arr2[i] == X:
#         now=i
#
# result=dfs(now)
# if result==1:
#     print("없음")
# else:
#     print(*result)

# --------------------------------------------------------------------------
# 4
# n=int(input())
# arr=[list(map(int,input().split())) for _ in range(n)]
#
# name = [x for x in range(n)] # 받은 숫자로 숫자배열 하나 생성!
#
# answer=[]
# def dfs(now):
#     global answer
#     answer.append(name[now])
#     for i in range(n):
#         if arr[now][i]==1:
#             dfs(i)
#
# dfs(0)  # 0번 인덱스 부터 깊이우선 탐색 시작
# print(*answer)

# -------------------------------------------------------------------------

# 5
# n=int(input())
# arr=[list(map(int,input().split())) for _ in range(n)]
#
# name = [x for x in range(n)] # 받은 숫자로 숫자배열 하나 생성!
#
# answer=[]
# def dfs(now):
#     global answer
#     if
#     # answer.append(name[now])
#     for i in range(n):
#         if arr[now][i]==1:
#             print(now,i)
#             dfs(i)
#
#
# dfs(0)  # 0번 인덱스 부터 깊이우선 탐색 시작

# ------------------------------------------------------------------------------
# 6
# name=list(input())
# arr=[list(map(int,input().split())) for _ in range(8)]
#
# answer=[]
# def dfs(now):
#     global answer
#     answer.append(name[now])
#     for i in range(8):
#         if arr[now][i]==1:
#
#             dfs(i)
#
#
# dfs(0)
# print(*answer,sep='')















