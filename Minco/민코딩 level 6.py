#1
# def INPUT_FUNC():
#     a,b = map(str,(input().split()))
#     return a,b
#
# call_func = INPUT_FUNC()
#
# def OUTPUT_FUNC():
#     print(*call_func)
#
# OUTPUT_FUNC()

#2----------------------------------------------------------------
# A,B,C = map(str,(input().split()))
#
# print(ord(A))
# print(ord(B))
# print(ord(C))

#----------------------------------------------------------------
#3
# num = int(input())
#
# for i in range(num):
#     for j in range(1,6):
#         print(j,end=" ")
#     print() # 여기서 프린트를 해줘야함

#-----------------------------------------------------------------
#4
# char = ["$","@","D","A","9","#"]
#
# for i in range(len(char)):
#     print(char[i],":",ord(char[i]),sep="")
#

#--------------------------------------------------------------
#5
# arr = ["B","T","K","A"]
# num = int(input())
#
# for i in range(num):
#     for j in range(len(arr)):
#         print(arr[j],end=' ')
#     print()
#

#-----------------------------------------------------------
#6
# txt = str(input())
#
# if txt.isupper() == True:
#     print("대문자입니다")
# else:
#     print("소문자입니다")

#----------------------------------------------------------------
#7
# num = int(input())
# for i in range(num):
#     for i in range(num):
#         print("#",end="")
#     print()

#------------------------------------------------------------------
#8
# char = str(input())
# print(ord(char)-43)

#---------------------------------------------------------
# 9
# print(chr(65))
# print(ord("A"))

# alpha = str(input())
#
# for i in range(65,ord(alpha)+1):
#     print(chr(i),end='')

#---------------------------------------------------------
# 10
# low = str(input())
# print(chr(ord(low)-32))

#---------------------------------------------------------
# 11
# ch1,ch2 = map(str,(input().split()))
#
# for i in range(4):
#     for i in range(ord(ch1),ord(ch2)+1):
#         print(chr(i),end=' ')
#     print()

#---------------------------------------------------------
# 12
# char = 'flag', 'a', 'b', 'c'
#
# def input_func() :
#     a,b,c = map(str,(input().split()))
#     return a,b,c
#
# a, b, c = input_func()
#
# def process(a,b,c) :
#     if a == 'A' and b == 'B'and c == 'C' :
#         flag = 1
#     return flag
#
# call_process = process(a,b,c)
# # print(call_process)
#
#
# def output_func(call_process):
#     if call_process == 1:
#         print("ABC를찾았다")
#     else:
#         print("못찾았다")
#
# output_func(call_process)

#----------------------------------------------------------------------------
# 13
# a,b,c = map(int,(input().split()))
#
# for i in range(c):
#     for j in range(a,b+1):
#         print(j,end=' ')
#     print()





