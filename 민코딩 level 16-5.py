#1
# a,b,c = map(int,(input().split()))
#
# for i in range(c):
#     for j in range(a,b+1):
#         print(j,end=' ')
#     print()

#-------------------------------------------
#2
# arrs = [[0]*3 for _ in range(6)]
# y,x = map(int,(input().split()))
#
#
# for j in range(3):
#     for i in range(6):
#         arrs[i][j] = chr(ord("A")+(5-i)+(2-j)*6)
#
# result=arrs[y][x]
#
# print(result)

#----------------------------------------
#3
# arr = [[0]*3 for _ in range(2)]
# num_list = list(map(int,input().split()))
#
# for i in range(2):
#     for j in range(3):
#         arr[i][j] = num_list[j+(3*i)]
#
# max_idx = -100000
# min_idx = 100000
#
# def max_func(max_idx):
#     for i in range(2):
#         for j in range(3):
#             if max_idx < arr[i][j]:
#                 max_idx = arr[i][j]
#                 x,y = i,j
#     return x,y
#
# call_max=max_func(max_idx)
# x,y=call_max
#
# def min_func(min_idx):
#     for i in range(2):
#         for j in range(3):
#             if min_idx > arr[i][j]:
#                 min_idx = arr[i][j]
#                 k,l = i,j
#     return k,l
#
# call_min = min_func(min_idx)
# k,l=call_min
#
# print(f'({x},{y})')
# print(f'({k},{l})')

#---------------------------------------------
#4
# a,b = map(int,(input().split()))
# arr = [0]*6
#
# arr[0] = a
# arr[1] = b
#
# for i in range(2,6):
#     arr[i] = arr[i-1]*arr[i-2]
#
#
# print(arr[6])

#---------------------------------------------
#5
# sentence=input()
# ch1,ch2 = input(),input()
# result=sentence.replace(ch1,ch2)
#
# print(result)

#------------------------------------------------------------
#6
# sentence=list(input())
#
# Max = -10000
# Min = 100000
# Max_index = 0
# Min_index = 0
#
# def max_func(Max,Max_index):
#     for i in range(len(sentence)):
#         if ord(sentence[i]) > Max:
#             Max = ord(sentence[i])
#
#     for j in range(len(sentence)):
#         if Max == ord(sentence[j]):
#             Max_index = j
#
#     return Max_index
#
# call_max = max_func(Max,Max_index)
#
#
# def min_func(Min,Min_index):
#     for i in range(len(sentence)):
#         if ord(sentence[i]) < Min :
#             Min = ord(sentence[i])
#
#     for j in range(len(sentence)):
#         if Min == ord(sentence[j]):
#             Min_index = j
#
#     return Min_index
#
# call_min = min_func(Min,Min_index)
#
#
# print(call_max)
# print(call_min)
#------------------------------------------------------------------------
#7
# arrs = [[0]*4 for _ in range(7)]
#
# for i in range(7):
#     for j in range(4):
#         arrs[i][j]=4*i+(j+1)
#
# a,b,c = map(int,(input().split()))
#
# for i in range(7):
#     if a == i or b == i or c == i :
#         for j in range(4):
#             arrs[i][j] = 0
#
# for row in arrs:
#     print(*row)

#------------------------------------------------------------------------------------
#8
# arrs = [["A","7","9","T","K","Q"],["M","I","N","C","O","D"]]
# a,b = input().split()
#
# def isExist(a,b):
#     if a in arrs[0] or a in arrs[1]:
#         print(f"{a} : 존재")
#     else:
#         print(f"{a} : 없음")
#
#     if b in arrs[0] or b in arrs[1]:
#         print(f"{b} : 존재")
#     else:
#         print(f"{b} : 없음")
#
# isExist(a,b)
#--------------------------------------------------------------------------
#9
# num1,num2,a = (input().split())
# num1 = int(num1)
# num2 = int(num2)
#
# #
# for i in range(num1):
#     for j in range(num2):
#         print(a,end='')
#     print()
#
# print()
#
# for i in range(num1):
#     for j in range(num2):
#         print(a,end='')
#     print()
#

