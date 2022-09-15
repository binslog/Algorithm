#2
# num = int(input())
#
# def abc(level):
#     global num
#     if level == 0:
#         print(num,end=' ') # 마지막 4
#         return
#     print(num,end=' ') # 4 3 2 1
#     num -= 1
#     abc(level-1)
#     num += 1
#     print(num,end=' ')
#
# abc(num)

#----------------------------------------------------------------

#3
# arr = list(map(int,input().split()))
#
# def abc(now):
#     if now == len(arr)-1:
#         print(arr[now], end=' ')
#         return
#
#     print(arr[now],end=' ')
#     abc(now+1)
#     print(arr[now], end=' ')
#
# abc(0)
#
#------------------------------------------------------------------
#4
# num = int(input())
#
# def abc(level):
#     global num
#     # print(num, end=' ')
#     if level == 3:
#         print(num, end=' ')
#         return
#     # print(num, end=' ')
#     num +=2
#     abc(level+1)
#     num -=2
#     print(num, end=' ')
# abc(0)

#------------------------------------------------------------------------------
#5
# arr = list(input())
#
# def abc(level):
#     if level == len(arr)-1:
#         print(arr[level], end='')
#         print()
#         print(arr[level], end='')
#         return
#     print(arr[level],end='')
#     abc(level+1)
#     print(arr[level],end='')
#
# abc(0)

#--------------------------------------------------------
#6
# a,b = map(int,(input().split()))
#
# def abc(a,b):
#     if a == b:
#         print(a,end=' ')
#         return
#     print(a, end=' ')
#     abc(a+1,b)
#     print(a, end=' ')
#
# abc(a,b)

#-------------------------------------------------------------
#7
# arr = [3,7,4,1,9,4,6,2]
# index = int(input())
#
# def abc(index):
#     if index==0:
#         print(arr[index],end=' ')
#         return
#     print(arr[index], end=' ')
#     abc(index-1)
#     print(arr[index], end=' ')
#
# abc(index)

#---------------------------------------------------------------
#8
# num = int(input())
#
# def abc(num):
#     if num == 0:
#         return
#     abc(num//2)
#     print(num,end=' ')
#
# abc(num)


