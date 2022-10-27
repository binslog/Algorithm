#1
# arr = [list(input()) for _ in range(4)]
#
# for i in range(4):
#     for j in range(3):
#         if arr[i][j] == "A":
#             y1,x1=i,j
#         if arr[i][j] == "B":
#             y2,x2=i,j
#
# result=abs(x1-x2)+abs(y2-y1)
# print(result)

#-----------------------------------------------------------
#2
# arr =[[3,4,1,5],[3,4,1,3],[5,2,3,6]]
# Sum=[0,0,0,0]
#
# for j in range(4):
#     for i in range(3):
#         Sum[j] += arr[i][j]
#
# index=int(input())
# print(Sum[index])

#---------------------------------------------------------------
# 3
# words = list(input())
# A,B = input().split()
#
# for i in range(len(words)-1):
#     if A==words[i] or B==words[i]:
#         words[i-1],words[i+1]="#","#"
#
# if words[-1] == A or words[-1] == B:
#     words[-2],words[0]="#","#"
#
# print(*words,sep='')

#-------------------------------------------------------------------
#4
# arr = [list(input()) for _ in range(4)]
#
# for i in range(2, -1, -1):
#     for j in range(3):
#         if arr[i][j] != '_':
#             cnt = 0
#             for k in range(i+1, len(arr)):
#                 if arr[k][j] == '_':
#                     cnt += 1
#             arr[i+cnt][j] = arr[i][j]
#             arr[i][j] = '_'
# for i in arr:
#     print(*i, sep ='')


# --------------------------------------------------------------
# 5
# arr = list(map(int,input().split()))
# bucket=[0]*10
#
# for i in range(len(arr)):
#     bucket[arr[i]] += 1
#
#
# result=[]
# for i in range(len(bucket)):
#     if bucket[i]!=0:
#         while bucket[i]>0:
#             result.append(i)
#             bucket[i]-=1
#
# print(*result)

#---------------------------------------------------------------------
# 6
# arr = [[1,5,3],[4,5,5],[3,3,5],[4,6,2]]
# a,b = map(int,(input().split()))
#
# for i in range(4):
#     for j in range(3):
#         if a<=arr[i][j] and arr[i][j]<=b:
#             arr[i][j]="#"
#
# for row in arr:
#     print(*row)

#------------------------------------------------------------------
# 7

arr=[[0,0,0,0,0,0,0],
     [0,0,"A",0,"A",0,0],
     [0,"A","B",0,"B","A",0],
     [0,0,"A","B","A",0,0],
     [0,0,"B","A",0,"A",0],
     [0,"A","A",0,0,0,0],
     [0,0,0,0,0,0,0]]

y,x = map(int,(input().split()))
arr[y][x] = "A"

directy=[-1,1,0,0]
directx=[0,0,-1,1]

def baduk(y,x):
    if arr[y][x] == "B":
        cnt=0
        for k in range(4):
            dk=directy[k]+y
            dl=directx[k]+x
            if arr[dk][dl] =="A":
                cnt +=1
                if cnt == 4:
                    return 1

result=0
for i in range(7):
    for j in range(7):
        ret = baduk(i,j)
        result+=int(ret)

print(result)


# ----------------------------------------------------------------
# 8
# arr = [['_','_','_'],
#        ['_','_','_'],
#        ['A','T','K'],
#        ['_','_','_'],
#        ['_','_','_']]
#
# com = [list(input().split()) for _ in range(7)]
#
# for i in range(7):
#     if com[i][1]=='UP':
#         com[i][0]























































