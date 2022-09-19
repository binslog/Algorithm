# 1
# arr=list(input())
# path=['']*4
# used=[0]*4
#
# def abc(level,start):
#     if level == 3:
#         for i in range(level):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(4):
#         if used[i] ==1: continue
#         else:
#             path[level]=arr[i]
#             used[i]=1
#             abc(level+1,i)
#             used[i]=0
#             path[level]=0
#
# abc(0,0)

# ---------------------------------------------
# 2
# arr = list(input())
# path=['']*4
# cnt=0
# def abc(level):
#     global cnt
#     if level == 4:
#         flag=True
#         for i in range(3):
#             if path[i] == "T" and path[i+1] == "B":
#                 flag=False
#                 break
#             if path[i] == "B" and path[i+1] == "T":
#                 flag=False
#                 break
#         if flag:
#             cnt+=1
#         return # 재귀 다시 돌아가고
#
#     for i in range(len(arr)):
#         path[level]=arr[i]
#         abc(level+1)
#
#     return cnt # 다 끝났으면 cnt 리턴하자
#
# result=abc(0)
# print(result)
#
# ---------------------------------------------

# 3
# arr = ["A","B","C"]
# num = int(input())
# path=['']*10
# cnt=0
# def abc(level):
#     global cnt
#     if level == num:
#         flag=True
#         for i in range(num-2):
#             if path[i] == path[i+1] == path[i+2]:
#                 flag=False
#                 break
#         if flag:
#             cnt+=1
#         return
#
#     for i in range(3):
#         path[level]=arr[i]
#         abc(level+1)
#
#     return cnt
#
# result=abc(0)
# print(result)

# ------------------------------------------------------
# 4
# arr = ["B","T","S","K","R"]
# path =['']*5
# used =['']*5
# cnt=0
# n = int(input())
#
# def abc(level):
#     global cnt
#     if level == n:
#         check = []
#         for i in range(n):
#             check.append(path[i])
#         if "S" in check:
#             cnt +=1
#         return
#
#     for i in range(5):
#         if used[i] == 1: continue
#         path[level]=arr[i]
#         used[i]=1
#         abc(level+1)
#         used[i]=0
#         path[level]=0
#
#     return cnt
#
# result=abc(0)
# print(result)

# --------------------------------------------------------------------------------
# 6
# arr = ["E","W","A","B","C"]
# path =['']*5
# used =['']*5
# ex = input()
#
# def abc(level):
#     if level == 4:
#         check = []
#         for i in range(4):
#             check.append(path[i])
#         if ex not in check:
#             for i in range(4):
#                 print(path[i],end='')
#             print()
#         return
#
#     for i in range(5):
#         if used[i] == 1: continue
#         path[level]=arr[i]
#         used[i]=1
#         abc(level+1)
#         used[i]=0
#         path[level]=0
#
# abc(0)

# -----------------------------------------------------------
# 7
words=input()
cnt=0
check=[]
def abc(level):
    global cnt,check
    if level == 4:
        cnt+= 1
        return

    for word in words:
        if level == 0 or abs(int(check[level-1]) - int(word)) <= 3:
            check.append(word)
            abc(level+1)
            check.pop()
abc(0)
print(cnt)





