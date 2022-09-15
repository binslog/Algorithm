#1

# def abc(level):
#     if level==2:
#         return
#
#     for i in range(3):
#         abc(level+1)
#
# abc(0)

#--------------------------------------------
#2
# ID = list("qlqlaqkq")
# PW = list("tkaruqtkf")
#
# input_id = list(input())
# input_pw = list(input())
#
# flag=0
#
# for i in range(len(input_id)):
#     if input_id[i] != ID[i]:
#         flag=1
#         break
#     else:
#         flag=0
#
# for i in range(len(input_pw)):
#     if input_pw[i] != PW[i]:
#         flag=1
#         break
#     else:
#         flag=0

#
# if flag:
#     print("INVALID")
# else:
#     print("LOGIN")

#---------------------------------------------------------
#3
# def abc(cur,depth):
#     global level,branch
#     if cur == level :
#         return
#     for i in range(branch):
#         abc(cur+1,depth)
#
#
# level = int(input())
# branch = int(input())
# abc(0,0)


#-------------------------------------------------------------------

#4
# def recur(cur, depth):
#     if cur > depth:
#         return
#     print(cur, end="")
#     for i in range(2):
#         recur(cur + 1, depth)
#
#
# N = int(input())
# recur(0, N)

#----------------------------------------------------------------
#5
# word1,word2,word3 = list(input()),list(input()),list(input())
#
# if len(word1)<len(word3):
#     word1,word3=word3,word1
#
# if len(word1)<len(word2):
#     word1,word2=word2,word1
#
#
# print(*word1,sep='')
# print(*word2,sep='')
# print(*word3,sep='')

#--------------------------------------------------------------
#6
# def abc(cur,depth):
#     global level,branch,cnt
#     cnt += 1
#     if cur == level :
#         return
#
#     for i in range(branch):
#         abc(cur+1,depth)
#
# branch,level = map(int,(input().split()))
# cnt=0
# abc(0,0)
# print(cnt)

#----------------------------------------------------------------------
# 7
# def recur(depth):
#     if depth==1:
#         print(depth,end=' ')
#         return
#     print(depth,end=' ')
#     recur(depth-1)
#     print(depth,end=' ')
#
#
# words = list(input())
# level = len(words)
# recur(level)

#----------------------------------------------------------------------
# 8
# N = int(input())
# command = [input() for _ in range(N)]
# y,x=5,5
#
# for com in command:
#     if com =='up':
#         y -= 1
#     if com =='down':
#         y += 1
#     if com == 'left':
#         x -= 1
#     if com =='right':
#         x += 1
#     if com =='click':
#         print("%d,%d" % (y,x))





