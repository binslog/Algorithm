#1
# def one():
#     num1 = int(input())
#     return num1
#
# num1 = one()
#
# def two():
#     num2 = str(input())
#     return num2
#
# num2 = two()
#
# print(num1,end='')
# print(num2,end='')
#--------------------------------------------------------------------

#2
# num=int(input())
# arr=[[0 for j in range(4)] for i in range(4)]
# # print(arr)
#
# if num % 2 == 0 :
#     for i in range(4):
#         for j in range(4):
#             if i == j :
#                 arr[i][j] = i+1
#
# else:
#     for i in range(4):
#         for j in range(4):
#             if i + j == 3:
#                 arr[i][j] = i+1
#
#
# for row in arr:
#     print(*row)

#-----------------------------------------------------------------------
#3
# def chicken():
#     num = int(input())
#     num += 10
#     return num
#
# chicken = chicken()
#
# def coke():
#     str2 = str(input())
#     return str2
#
# coke = coke()
#
# def KFC(chicken,coke):
#     a=chicken
#     b=coke
#     return a,b
#
# KFC_CALL=KFC(chicken,coke)
#
# def main():
#     return KFC(chicken,coke)
#
# call_main=main()
#
# for row in call_main:
#     print(row,end='')
#------------------------------------------------------------------------

#4
# def getChar():
#     A, B = map(str, input().split())
#     if A>B :
#         return A
#     else:
#         return B
#
# def main():
#     abc = getChar()
#     return abc
#
# result=main()
# print(result)

#-------------------------------------------------------------------------
#5
# num = int(input())
# arr = [[0 for j in range(3)] for i in range(3)]
#
#
# if num % 5 == 1:
#     index = 1
#     for j in range(2,-1,-1):
#         index += 3 * (2-j)
#         for i in range(2,-1,-1):
#             arr[i][j] = (2-i) + index
#             if i == 0:
#                 index = 1
#
# if num % 5 == 2:
#     index = 1
#     for i in range(2,-1,-1):
#         index += 3 * (2-i)
#         for j in range(3):
#             arr[i][j] = j + index
#             if j == 2:
#                 index = 1
#
# else:
#     index = 10
#     for j in range(3):
#         index += 3 * j
#         for i in range(3):
#             arr[i][j] = i + index
#             if i ==2 :
#                 index  = 10
#
# for row in arr :
#     print(*row)


#------------------------------------------------------------------------

#6

# def main():
#     a,b = map(int,input().split())
#     c = a/b
#     if c % 2 == 0 :
#         return even(c)
#     else:
#         return even(c)
#
#
#     return printData(a+b)
#
# main= main()
#
# def even(c):
#       even_data = c * 2
#     return printData(even_data)
#
# even = even(c)
# def odd(c)
#     odd_data = c - 10
#     return printData(odd_data)
#
# odd = odd(c)
# def printData(main,even,odd):
#     print(main,even,odd)
#
# printData(main,even,odd)

#-----------------------------------------------------------------------
#7
# def GOP():
#     a,b = map(int,input().split())
#     c = a*b
#     return c
#
# multiple = GOP()
# # print(multiple)
# def SUM():
#     d,e = map(int,input().split())
#     f = d+e
#     return f
#
# sum = SUM()
# # print(sum)
#
#
# def Main(multiple,sum):
#     if multiple == sum :
#         print("GOP==SUM")
#
#     elif multiple>sum :
#         print("GOP>SUM")
#
#     else:
#         print("GOP<SUM")
#
# Main(multiple,sum)

#----------------------------------------------------------------------------------
#8


# def main():
#     stone = int(input())
#     pingpong(stone)
#     return stone
#
# stone=main()
#
# def pingpong(stone):
#     tong = stone + 10
#     main(tong)
#     return tong
#
# tong = pingpong(stone)
# def output(tong):
#     ret = tong
#     print(ret)
#
# output(tong)

#-------------------------------------------------------------------
#9
# arr = [[0 for j in range (4)] for i in range(4)]
# # print(arr)
# index = 1
#
# for j in range(3,-1,-1):
#     index += 4*(3-j)
#     for i in range(4):
#         arr[i][j] = i + index
#         if i == 3 :
#             index = 1
#
# for row in arr:
#     print(*row)

#-------------------------------------------------------------------------------------

#10
# num = int(input())
# arr = [[0 for j in range(4)] for i in range(3)]
#
# index = 1
# for i in range(2,-1,-1):
#     index += 4*(2-i)
#     for j in range(3,-1,-1):
#         arr[i][j] = index + 3-j
#         if j == 0:
#             index = 1
#
#
# for j in range(4):
#     for i in range(3):
#         if j == num :
#             arr[i][j] = 0
#
# for row in arr:
#     print(*row)

#--------------------------------------------------------------------------------------------
#11
# arr = [[3,8,10,2],
#        [3,5,8,7],
#        [2,8,6,4],
#        [1,3,0,9]
#       ]

# arr = [list(map(int,input().split()))for _ in range(4)]
#
# for i in range(4):
#     for j in range(4):
#         if arr[i][j] == 0 :
#             arr[i][j] = "!"
#         elif arr[i][j] % 2 == 0:
#             arr[i][j] = "#"
#         elif arr[i][j] % 2 == 1:
#             arr[i][j] = "@"
#
#
# for row in arr:
#     print(*row,sep='')

#--------------------------------------------------------
#12

def input_func():
    num = int(input())
    return num

num = input_func()

def countdown_func(num):
    for i in range(num,0,-1):
        print(i,end=' ')

countdown_func(num)











