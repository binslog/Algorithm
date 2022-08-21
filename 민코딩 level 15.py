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




















