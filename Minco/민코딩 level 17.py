#1
# arr =['M','T','K','C']
# a = input()
#
# def isExist(arr,a):
#     if a in arr:
#         print("발견")
#     else:
#         print("미발견")
#
# isExist(arr,a)

#------------------------------------------------------------------------------------
#2
# arr = [5,9,4,6,1,5,8,9]
# index, target = map(int,input().split())
#
# for i in range(len(arr)):
#     if arr[i] == target :
#         print(i-index)

#----------------------------------------------------------------------------------
#3
# arr = [[3,5,9],[4,2,1],[1,1,5]]
# color_arr = [list(map(int,input().split())) for _ in range(3)]
# result = 0
#
# for i in range(3):
#     for j in range(3):
#         if color_arr[i][j] == 1 :
#             result += arr[i][j] + 1
#
# print(result)

#----------------------------------------------------------------------------------
#4
# arr =[['A','T','K','B'],['C','Z','F','D'],['H','G','E','I']]
# a,y,x = input().split()
# y = int(y)
# x = int(x)
#
# for i in range(3):
#     for j in range(4):
#         if a == arr[i][j]:
#             result = arr[i+y][j+x]
#
# print(result)

#----------------------------------------------------------------------------------
# #5
# arr = [[3,5,9],[4,2,1],[5,1,5]]
# num1, num2, num3 = map(int,(input().split()))
# flag1,flag2,flag3=0,0,0
#
# for i in range(3):
#     if num1 in arr[i]:
#         flag1=1
#         break
#     else:
#         flag1=0
#
#
# for i in range(3):
#     if num2 in arr[i]:
#         flag2=1
#         break
#     else:
#         flag2=0
#
#
# for i in range(3):
#     if num3 in arr[i]:
#         flag3=1
#         break
#     else:
#         flag3=0
#
# if flag1 :
#     print(f'{num1}:존재')
# else:
#     print(f'{num1}:미발견')
#
# if flag2 :
#     print(f'{num2}:존재')
# else:
#     print(f'{num2}:미발견')
#
# if flag3 :
#     print(f'{num3}:존재')
# else:
#     print(f'{num3}:미발견')

#----------------------------------------------------------------------------
#6
# mask1 = [[0,0,0,1],[1,1,0,1],[1,0,0,1],[1,1,1,1]]
# mask2 = [[1,1,1,1],[1,0,1,1],[1,0,0,0],[1,0,0,0]]
# mask3 = [[0]*4 for _ in range(4)]
#
# for i in range(4):
#     for j in range(4):
#         mask3[i][j] = mask1[i][j]+mask2[i][j]
#
# # print(mask3)
#
# for i in range(4):
#     for j in range(4):
#         if mask3[i][j]==0:
#             print(f"({i},{j})")

#-----------------------------------------------------------------------------
#7
# mask1 = [[0,0,1,0,0],[0,0,1,1,1]]
# mask2 = [[3,5,4,1,1],[3,5,2,5,6]]
#
# num = int(input())
# flag =0
#
# for i in range(2):
#     for j in range(5):
#         if mask2[i][j] == num and mask1[i][j] == 1:
#             flag = 1
#             break
#         else:
#             flag = 0
#
# if flag==1:
#     print(f'{num} 존재')
# else:
#     print(f'{num} 없음')

#--------------------------------------------------------------------
#8
# arr = ["B","T","K","I","G","Z"]
# target = list(input().split())
# cnt =0
#
# for i in range(4):
#     if target[i] in arr :
#       cnt += 1
#
# print(cnt)


#-------------------------------------------------------------------
#9
# arr = [[3,7,4],[2,2,4],[2,2,5]]
# target = list(map(int,input().split()))
# target_dict = {target[0]:0,target[1]:1,target[2]:2}
#
# for i in range(3):
#     for j in range(3):
#         if target[0] == arr[i][j] :
#             target_dict[target[0]] += 1
#
#         elif target[1] == arr[i][j] :
#             target_dict[target[1]] += 1
#
#         elif target[2] == arr[i][j] :
#             target_dict[target[2]] += 1
#
# # print(target_dict)
# result = max(target_dict.values())
#
# for key, value in target_dict.items():
#      if value == result:
#          print(key)
#          break














































