#1
# num = str(input())
# print(num * 3)
#---------------------------------------------------------
#2
# arr = list(map(int,input().split()))
# result=0
# for i in range(len(arr)):
#     result +=arr[i]
# print(result)

#------------------------------------------------------------
#3
# arr = ['m','i','n']
# index = int(input())
#
# print(arr[index])

#------------------------------------------------------------
#4
# num = int(input())
# def KFC() :
#     print("KFC입니다")
#
# def MC():
#     print("MC입니다")
#
# if num ==1 :
#     KFC()
# elif num==2 :
#     MC()

#--------------------------------------------------
#5
# def LOT():
#     for i in range(1,6):
#         print(i,end='')
#
# LOT()
# LOT()
# LOT()


#-----------------------------------
#6
# def KFC():
#     print("#"*10)
# def MC():
#     print("@"*10)
#
# def main():
#     KFC()
#     MC()
#
# main()

#------------------------------------------
#7
# arr = [0] * 6
#
# a,b,c= map(int,input().split())
# d = int(input())
#
# arr[0]=a
# arr[1]=b
# arr[2]=c
# arr[3]=d
# arr[4]=d+1
# arr[5]=d+2
#
# print(*arr)

#---------------------------------------------------------
#8
# def KFC():
#     num = int(input())
#     return num
#
# def BBQ(num):
#     if num > 5 :
#         print("만세")
#     else:
#         print("다시")
#
# call_kfc = KFC()
# num = call_kfc
#
# call_bbq = BBQ(num)

#------------------------------------------
#9.
# arr = ['A','B','C']
#
# def main():
#     num = int(input())
#     return num
#
# num = main()
#
# def KFC():
#     for i in range(3):
#         print(arr[i],end='')
#
#
# KFC()
# KFC()
# KFC()
#
# # for i in range()

#----------------------------------------
#10
# def input_func():
#     arr = list(map(int,input().split()))
#
#     return arr
#
# arr = input_func()
#
# def output_func():
#     for i in range(3,-1,-1):
#         print(arr[i],end='')
#
# output_func()

#-------------------------------------------------
#11

# arr = [0] * 6
#
# def main() :
#     num = int(input())
#     for i in range(6):
#         arr[i] = num + i
#
#     return arr
#
# call_main = main()

# def PrintAll():
#     for i in range(6):
#         print(call_main[i])
#
# PrintAll()

#-----------------------------------------------------
#12
# def QTR():
#     print("QTR100%")
#
# def BBQ():
#     print("BBQ100%")
#
# arr = list(map(int,input().split()))
# sum = 0
#
# for i in range(len(arr)):
#     sum += arr[i]
#
# if sum >= 10 :
#     QTR()
# else:
#     BBQ()

#---------------------------------------------------------
#13
# arr=[3,4,1,5,8,1,7,7,3,6,9]
# num = int(input())
#
# for i in range(0,11,num):
#     print(arr[i],end=' ')









#12