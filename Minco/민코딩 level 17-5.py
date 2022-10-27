#1
# arr = [3,4,1,1,2,6,8,7,8,9,10]
# startindex = int(input())
#
# def getSum(arr,startindex):
#     sum = 0
#     for i in range(startindex,startindex+5):
#         sum += arr[i]
#
#     print(sum)
#
# getSum(arr,startindex)

#-------------------------------------------------------------------------------
#2
# arrs = [3,7,4,1,2,6]
# univer_arr = [list(map(int,input().split())) for _ in range(2)]
# result_arr = [[0]*2 for _ in range(2)]
#
# for i in range(2):
#     for j in range(2):
#         if univer_arr[i][j] in arrs:
#             result_arr[i][j] = "OK"
#         else:
#             result_arr[i][j] = "NO"
#
# for row in result_arr:
#     print(*row)

#-------------------------------------------------------------------------------
#3
# a,b = input(),input()
#
# def isSame(a,b):
#     if a==b :
#         return 1
#     else:
#         return 0
#
# call_isname = isSame(a,b)
#
# if call_isname == 1:
#     print("동명")
# else:
#     print("남남")

#---------------------------------------------------------------------------------
#4
# arr = [["G","K","T"],["P","A","C"]]
# a,b = input().split()
#
#
# def isExist(arr,a,b):
#     result_arr=[]
#     if (a in arr[0]) or (a in arr[1]):
#         result_arr.append("a")
#     if (b in arr[0]) or (b in arr[1]):
#         result_arr.append("b")
#     return result_arr
#
# result = isExist(arr,a,b)
# # print(result)
#
# if "a" in result and "b" in result:
#     print("대발견")
# elif "a" not in result and "b" not in result:
#     print("미발견")
# else:
#     print("중발견")

#-------------------------------------------------------------------------------------
#5
# vect = [3,5,4,2,6,6,5]
# bit = list(map(int,input().split()))
# result = []
#
# for i in range(len(bit)):
#     if bit[i] == 0:
#         result.append(0)
#     else:
#         result.append(7)
#
# for row in result:
#     print(row,end='')

#-------------------------------------------------------------------------------------
#6
# password = [3,7,4,9]
# ipt_arr = list(map(int,input().split()))
# flag = 0
#
# def isSame(flag):
#     for i in range(4):
#         if password[i] == ipt_arr[i]:
#             flag=1
#         else:
#             flag=0
#             break
#
#     return flag
#
# call_issame = isSame(flag)
#
# if call_issame == 1:
#     print("pass")
# else:
#     print("fail")

#----------------------------------------------------------------------------------
# 7
# levelTable = [[10,20],[30,60],[100,150],[200,300]]
# fruits = list(map(int,input().split()))
# dict_result = {"lev0":0, "lev1":0, "lev2":0, "lev3":0 }
#
# for i in range(6):
#     if fruits[i]>= 10 and fruits[i] <= 20 :
#         dict_result["lev0"] +=1
#
#     if fruits[i]>= 30 and fruits[i] <= 60 :
#         dict_result["lev1"] +=1
#
#     if fruits[i]>= 100 and fruits[i] <= 150 :
#         dict_result["lev2"] +=1
#
#     if fruits[i]>= 200 and fruits[i] <= 300 :
#         dict_result["lev3"] +=1
#
# for key, value in dict_result.items():
#     print(f'{key}:{dict_result[key]}')

#----------------------------------------------------------------------------------
# 8
# Map = [[3,55,42],[-5,-9,-10]]
# pix = [list(map(int,input().split())) for _ in range(2)]
# result = [[0]*2 for _ in range(2)]
#
# for i in range(2):
#     for j in range(2):
#         if pix[i][j] in Map[0] or pix[i][j] in Map[1]:
#             result[i][j] = "Y"
#         else:
#             result[i][j] = "N"
#
# for row in result:
#     print(*row)

#----------------------------------------------------------------------------------
# 9
numbers = list(map(int,input().split()))

Min = 21e8
idx = 0

for i in range(0,6,2):
    if numbers[i] < Min:
        Min = numbers[i]
        idx = i

print(f'arr[{idx}]={numbers[idx]}')





#----------------------------------------------------------------------------------
# 10
# arrs = [[3,1,9],[7,2,1],[1,0,8]]
# mask = [list(map(int,input().split())) for _ in range(3)]
# flag = 0
#
# for i in range(3):
#     for j in range(3):
#         if mask[i][j] == 1 :
#             if arrs[i][j] >= 3 and arrs[i][j] <= 5:
#                 flag = 1
#                 break
#             break
#         else:
#             flag = 0
#
# if flag :
#     print("발견")
# else:
#     print("미발견")

#------------------------------------------------------------------------------
# 11
# arrs = [3,5,4,2]
# mask = list(map(int,input().split()))
# sum = 0
#
# for i in range(4):
#     if mask[i] == 1:
#         sum += arrs[i]
#
#
# print(sum)

#----------------------------------------------------------------------------
#12
# arrs = [["A","B","C","D","E"], ["F","G","H","I","J"],
#         ["K","L","M","N","O"],["P","Q","R","S","T"],
#         ["U","V","W","X","Y"]]
#
# a = input()
# y,x = 0,0
#
# for i in range(5):
#     for j in range(5):
#         if arrs[i][j] == a :
#             y,x = i-2,j-2
#
# print(f'{y},{x}')

