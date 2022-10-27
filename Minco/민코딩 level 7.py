# 1
# arr1 = [3,5,2,4,1]
# arr2 = [[9,8],
#         [7,1],
#         [3,4]
#         ]
# num = int(input())
#
# if num % 2 == 0 :
#     for row in arr2 :
#         print(*row,sep='')
# else:
#     print(*arr1,sep='')

#------------------------------------------------
#2
# a,b = map(int,(input().split()))
#
# if abs(a-b) % 2 == 0 :
#     print("짝사랑만")
# else:
#     print("고백한다")

#---------------------------------------------------------------
#3
# arr = [[3,1,1],[2,3,2]]
# result = []
#
# for i in range(2) :
#     for j in range(3):
#         result = arr[i][j]
#         print(result,end = ' ')
#
#

#----------------------------------------------------------------
#4
# arr =list(map(int,input().split()))
# arrs = [3,4,5,6,7]
# count = 0
#
# for i in range(len(arr)) :
#     if arr[i] in arrs :
#         count += 1
#
# print(count)

#-----------------------------------------------------------------
#5

# num = int(input())
#
# if num >= 80 :
#     print("수")
# elif num >= 70 :
#     print("우")
# elif num >= 60 :
#     print("미")
# else:
#     print("재시도")

# elif 를 쓰면 중복 피할 수 있다.

#------------------------------------------------------------
#6
# num = list(map(int,input().split()))
#
# for i in range(4):
#     if num[i] > 20 :
#         print("더 작은수를 입력하세요")
#     elif num[i] < 20 :
#         print("더 큰수를 입력하세요")
#     elif num[i] == 20:
#         print("정답입니다")

#-------------------------------------------------------------
#7
# a,b,c = map(int,input().split())
#
# if a>=b and a>=c :
#     print(f"MAX={a}")
# elif b>=a and b>=c:
#     print(f"MAX={b}")
# else:
#     print(f"MAX={c}")
#
# if a<=b and a<=c :
#     print(f"MIN={a}")
# elif b<=a and b<=c:
#     print(f"MIN={b}")
# else:
#     print(f"MIN={c}")

#---------------------------------------------------------------
#8
# arr = [[3,4,1],[2,1,4],[3,3,0]]
# odd_count=0
# even_count=0
#
# for i in range(3):
#     for j in range(3):
#         if arr[i][j] % 2 == 0 :
#             even_count +=1
#         else:
#             odd_count +=1
#
#
# print(f"짝수 : {even_count}")
# print(f"홀수 : {odd_count}")

#------------------------------------------------------------------
#9
# arr = list(map(int,input().split()))
#
#
# for i in range(5):
#     if arr[i] >= 70:
#         print(f"{i+1}번사람은{arr[i]}점PASS")
#
#     elif arr[i] >= 50:
#         print(f"{i+1}번사람은{arr[i]}점RETEST")
#
#     else:
#         print(f"{i+1}번사람은{arr[i]}점FAIL")

#--------------------------------------------------------------------
#10
# A = str(input())
#
# def input_func(A):
#     arr = [[A for j in range(4)] for i in range(4)]
#     return arr
#
# arrs = input_func(A)
#
#
# def ouput_func(arrs):
#     for row in arrs:
#         print(*row,sep='')
#
#
# ouput_func(arrs)

#-------------------------------------------------------------------
#11

# def input_func():
#     num = int(input())
#     return num
#
# num = input_func()
#
# def process(num):
#     index = 0
#     arr=[[0 for j in range(3)] for i in range(3)]
#     for i in range(3):
#         index = i*3
#         for j in range(3):
#             arr[i][j] += num+j+index
#
#     return arr
#
# arr = process(num)
#
# def output(arr):
#
#     for row in arr:
#         print(*row,sep=' ')
#
# output(arr)

#-------------------------------------------------------------------------
#12
num = int(input())

def BBQ():
    if num > 0 and num < 5 :
        print("초기값")
    elif num > 6 and num < 10 :
        print("중간값")
    else:
        print("알수없는값")



if num == 3 or num ==5 or num ==7:
    for i in range(11):
        print(i,end='')

elif num == 0 or num == 8 :
    for i in range(10,0,-1):
        print(i,end='')

else:
    BBQ()





















