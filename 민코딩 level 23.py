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
#         for i in range(3):
#             if arr[i] == "T" and arr[i+1] == "B": continue
#             if arr[i] == "B" and arr[i+1] == "T": continue
#             else:
#                 cnt+=1
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
#
# ---------------------------------------------

# 3
arr = ["A","B","C"]
num = int(input())
path=['']*10
cnt=0
def abc(level):
    global cnt
    if level == num:
        for i in range(num-2):
            if path[i] == path[i+1] == path[i+2]:break
            else:
                cnt+=1
        return

    for i in range(3):
        path[level]=arr[i]
        abc(level+1)

    return cnt

result=abc(0)
print(result)
















