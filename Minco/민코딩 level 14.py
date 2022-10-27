# #1
# a,b = map(int,input().split())
#
# while a <= b : # 조건설정하는거 생각!!
#     print(a,end=' ')
#     a = a+1


#-------------------------------------------------------

#2
# arr = [list(map(int,input().split())) for _ in range(5)]
# sum =[0]*5
#
# for i in range(5):
#
#     for j in range(4):
#         sum[i] += arr[i][j]
#
#
# print(*sum)

#---------------------------------------------------------
#3
# arr = list(map(str,input().split()))
#
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         print(arr[j],end=' ')
#     print()

#---------------------------------------------------------
#4
# arr = [list(map(int,input().split())) for _ in range(3)]
# sum = 0
#
# for i in range(3):
#     for j in range(3):
#        if j == 0 or i == j :
#            sum += arr[i][j]
#        elif i == 2 and j == 1:
#            sum += arr[i][j]
#
# print(sum)

#----------------------------------------------------------
#5
# vect = [3,5,1,1,2,3,2]
# arr = list(map(int,input().split()))
# cnt = [0]*4
#
# for i in range(4):
#     for j in range(7):
#         if arr[i] == vect[j] :
#             cnt[i] += 1
#
# for i in range(4):
#     print(f'{arr[i]}={cnt[i]}개')

#-------------------------------------------------------------
#6
# A_list = list(map(int,input().split()))
# S_list = [0]
# n = 0
#
# while A_list :
#     for i in range(len(A_list)):
#         if S_list[n] < A_list[i]:
#             S_list[n] = A_list[i]
#     A_list.remove(S_list[n])
#
#     if A_list ==[]:
#         break
#     n+= 1
#     S_list.append(0)
#
# print(*S_list,sep='')

#--------------------------------------------s-------------------------
#7
# a = list(input())
#
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]     # swap
#
# for i in a:
#     print(i,end='')


#---------------------------------------------------------------------
#8
# vect = [10,50,40,20,30,40]
# arr = list(map(int,input().split()))
# cnt = [0]*6
#
# for i in range(6):
#     for j in range(6):
#         if arr[i] < vect[j] :
#             cnt[i] += 1
#
# for i in range(6):
#     print(f'{arr[i]}={cnt[i]}개')
















