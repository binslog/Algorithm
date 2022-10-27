#1
# str1 = str(input())
# str2 = str(input())
# com = 0
#
# if len(str1) != len(str2) :
#     print("다름")
# elif len(str1) == len(str2) :
#     for i in range(len(str1)):
#         if str1[i] == str2[i] :
#             continue
#             print("같음")
#         else:
#             print("다름")

#------------------------------------------------------------------
#2
# num = int(input())
# arr = [0]*4
#
# arr[0] = num // 1000
# arr[1] = (num-(arr[0]*1000)) // 100
# arr[2] = (num-(arr[0]*1000+arr[1]*100)) // 10
# arr[3] = num % 10
#
#
# for row in arr:
#     print(f'숫자{row}')
#

#----------------------------------------------------------------------

#3
# arr = list(map(int,input().split()))
# flag=0
#
# for i in range(1,6):
#     if abs(arr[i-1]-arr[i]) < 3 :
#         flag=1
#     else:
#         flag=0
#         break
#
#
# if flag == 1:
#     print("완벽한배치")
# else:
#     print("재배치필요")


#-------------------------------------------------------------------------
#4
# a = list(str(input()))
# b = list(str(input()))
# flag = 1
#
# for i in range(len(a)-1,-1,-1):
#     if a[i]==b[(len(a)-1)-i] :
#         flag = 1
#     else:
#         flag = 0
#         break
#
# if flag == 1 :
#     print("거울문장")
# else:
#     print("거울문장아님")

#--------------------------------------------------------------------------
#5
# arr = [list(input()) for _ in range(4)]
# arr2 = [0] * 4
#
# for i in range(len(arr)):
#      arr2[i] = len(arr[i])
#
# arr2=sorted(arr2)
# # print(arr2,end=' ')
#
# print(*arr2)


#--------------------------------------------------------------------------
#6
# A = list(input())a_list = []
#
#
# for i in range(len(A)):
#     if i % 2 == 1:
#         if A[i].islower() == True :
#             a_list.append(1)
#
#     elif i % 2 == 0:
#         if A[i].isupper() == True :
#             a_list.append(2)
#
#     else:
#         a_list.append(3)
#
#
# if 3 in a_list:
#     print("일반문장")
# else:
#     print("개구리문장")
#

#--------------------------------------------------------------------------
#7
# arr = ['A','B','C','Z','E','T','Q']
# arr2 = list(map(str,input()))
#
# for i in range(len(arr2)) :
#
#     if arr2[i] in arr :
#         print(f"{arr2[i]}=마을사람")
#
#     else:
#         print(f"{arr2[i]}=외부사람")

#-----------------------------------------------------------------------------
#8
# arrs = [list(input()) for i in range(5)]
# len_arrs =[0]*5
# max = -1000
# max_idx = 0
#
# for i in range(5):
#     len_arrs[i]=len(arrs[i])
#
# for j in range(5):
#     if max < len_arrs[j]:
#         max = len_arrs[j]
#         max_idx = j
#
# print(*arrs[max_idx],sep='')

#-------------------------------------------------------------------------------
#9
# A = "BBQWORLD"
# B = "KFCAPPLE"
# C = "LOT"
#
#
# txt = input()
# cnt = 0
#
# for num in A :
#     if num == txt :
#         cnt += 1
#
# for num in B :
#     if num == txt :
#         cnt += 1
#
# for num in C :
#     if num == txt :
#         cnt += 1

# print(cnt)

#----------------------------------------------------------------------------
# #10.
# arr = [[0]*10]*3
# a,b,c = input(), input(), input()
#
# def countline(a,b,c):
#     print(f'{len(a)}={a}')
#     print(f'{len(b)}={b}')
#     print(f'{len(c)}={c}')
#
#
# countline(a,b,c)
#
#----------------------------------------------------------------------------
#11
# S = [list(input()) for _ in range(4)]
# new_list = []
# for i in range(len(S)):
#     if 'A' in S[i] or 'B' in S[i]:
#         if 'A' in S[i]:
#             new_list.append('A')
#         else:
#             new_list.append('B')
#
# if 'A' in new_list and 'B' in new_list:
#     print("대발견")
# elif'A' in new_list or 'B' in new_list:
#     print("중발견")
# else:
#     print("미발견")
#----------------------------------------------------------------------------------------------------
#12
# a,b = list(input()), list(input())
# char = [0] * 12
#
# for i in range(len(a)):
#     char[i]=a[i]
#
# for j in range(len(a),len(a)+len(b)):
#     char[j]=b[j-len(a)]
#
#
# for row in range(len(a)+len(b)):
#     print(char[row],end='')

#-------------------------------------------------------
#13
# arr=[["D","A","T","A","W"],["B","B","Q","K"]]
# num = int(input())
#
# if num%2 == 1 :
#     arr[0].sort()
# else:
#     arr[1].sort()
#
# for row in arr:
#     print(*row,sep='')

#---------------------------------------------
#14
#
# arr = [["P","O","T","I","O"],["A","B","C","D","E"],["Y","O","U","R","E"]]
# a,b = map(int,input().split())
# result=[]
#
# for i in range(3):
#     for j in range(a,b+1):
#         result.append(arr[i][j])
#
# print(*result,sep='')
#



#---------------------------------
#15
# a,b = input(),input()
#
# arrs=[list(a),list(b)]
# # print(arrs)
# cnt=0
#
# if len(a)>=len(b):
#     for i in range(len(arrs[1])):
#         if arrs[0][i] != arrs[1][i]:
#             cnt+=1
#     cnt += len(arrs[0]) - len(arrs[1])
#
# else:
#     for i in range(len(arrs[0])):
#         if arrs[0][i] != arrs[1][i]:
#             cnt+=1
#     cnt += len(arrs[1]) - len(arrs[0])
#
# print(cnt)














#---------------------------------
#16
# arr = [[""]*3 for _ in range(3)]
# a = input()
# b = 2
# cnt = 0
# while b >= 0:
#     c = 0
#     while c < 3 - b:
#         # print(b)
#         arr[b][c] = chr(ord(a) + cnt)
#         cnt = cnt + 1
#         c = c + 1
#     b = b - 1
#
# for row in arr:
#     print(*row,sep='')

















