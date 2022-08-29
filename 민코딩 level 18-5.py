#1
# arr = [["G","K","G"],[0,0,0]]
# lst = list(input().split())
#
# for i in range(2):
#     for j in range(3):
#         if i == 1:
#             arr[1][j] = lst[j]
#
# bucket = [0] * 100
#
# for i in range(2):
#     for j in range(3):
#         bucket[ord(arr[i][j])] += 1
#
# # print(bucket)
# flag=0
# for i in range(len(bucket)):
#     if bucket[i] >= 3:
#         flag=1
#         break
#     else:
#         flag=0
#
# if flag:
#     print("있음")
# else:
#     print("없음")

#------------------------------------------------------------------
#2
# arr = list(map(int,input().split()))
# bucket = [0] * 10
#
# for i in range(len(arr)):
#     bucket[arr[i]] += 1
#
# flag=1
# for i in range(len(bucket)):
#     if bucket[i]>=2:
#         flag=1
#         break
#     else:
#         flag=0
#
# if flag:
#     print("도플갱어 발견")
# else:
#     print("미발견")

#----------------------------------------------------------------------
#3
# arr = list(input())
# bucket = [0]*100
#
# for i in range(len(arr)):
#     bucket[ord(arr[i])] +=1
#
# Max = -100000
#
# for i in range(len(bucket)):
#     if Max < bucket[i]:
#         Max = bucket[i]
#         index = i
#
# # print(index)
# print(chr(index))

#------------------------------------------------------------------------
#4
# up = list(map(int,input().split()))
# down = list(map(int,input().split()))
# cnt =0
#
# for i in range(5):
#     if up[i] == 1 and down[i]==1:
#         cnt+=1
#
# print(f'{cnt}개')

#-------------------------------------------------------------------------
#5
# A = "ATKPTCABC"
# A_list = list(A)
#
# a,b = input().split()
#
# for i in range(len(A_list)):
#     if a==A_list[i]:
#         x=i
#         break
#
# for i in range(len(A_list)):
#     if b==A_list[i]:
#         y=i
#
#
# print(y-x)

#------------------------------------------------------------------------------
#6
# win = [[3,5,1],[4,2,6]]
# people = list(map(int,input().split()))
#
# bucket = [0] * 10
#
# for i in range(2):
#     for j in range(3):
#         bucket[win[i][j]] +=1
#
# for i in range(len(people)):
#     if bucket[people[i]] == 1:
#         print(f'{people[i]}번 합격')
#
#     else:
#         print(f'{people[i]}번 불합격')

#------------------------------------------------------------------------------
#7
# vect = list("MINCODING")
# n = int(input())
# lst = list(input().split())
#
# bucket = [0] * 100
#
# for i in range(len(vect)):
#     bucket[ord(vect[i])] += 1
#
# for i in range(len(lst)):
#     if bucket[ord(lst[i])] != 0 :
#         print("O",end='')
#     else:
#         print("X",end='')
#

#-------------------------------------------------------------------------------
# #8
# lst = [list(input()) for _ in range(3)]
# # print(lst)
# bucket = [0]*100
#
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         bucket[ord(lst[i][j])] += 1
#
# flag = 0
# for i in range(len(bucket)):
#     if bucket[i] > 1:
#         flag=1
#         break
#     else:
#         flag=0
#
#
# if flag:
#     print("No")
# else:
#     print("Perfect")


#-----------------------------------------------------------------------------------
#9
# arr = list(input())
# bucket = [0] * 100
# result=[]
#
# for i in range(len(arr)):
#     bucket[ord(arr[i])] +=1
#
# for i in range(len(bucket)):
#     if bucket[i] != 0 :
#         result.append(i)
#
# for row in result:
#     print(chr(row),end='')

#-------------------------------------------------------------
#10
# matrix = list(input())
# bucket = [0] * 100
#
# for i in range(len(matrix)):
#     bucket[ord(matrix[i])] +=1
#
# for i in range(len(bucket)):
#     if bucket[i] != 0 :
#         print(f'{chr(i)}:{bucket[i]}')

#------------------------------------------------------------
#11
# arr = list(input())
# word = ["G","H","O","S","T"]
#
# flag = 0
#
# for i in range(len(arr)):
#     for j in range(5):
#         if arr[i] != word[j]:
#             continue
#
#         elif arr[i] == word[j] :
#             flag +=1
#
# if flag == 5:
#     print("존재")
# else:
#     print('존재하지 않음')




























