# #1
# record = [[65000,35,42,70],[70,35,65000,1300],[65000,30000,38,42]]
# bucket = [0]* 100000
#
# for i in range(3):
#     for j in range(4):
#         bucket[record[i][j]]+=1
#
# max = -99999999
#
# for i in range(len(bucket)):
#     if max < bucket[i]:
#         max = bucket[i]
#
# for i in range(len(bucket)):
#     if bucket[i] == max:
#         print(i)

#----------------------------------------------------------------------
#2
# arrs = [list(map(int,input().split())) for _ in range(3)]
# bucket = [0] * 10
# result = []
#
# for i in range(3):
#     for j in range(3):
#         bucket[arrs[i][j]] += 1
#
# for k in range(1,len(bucket)):
#     if bucket[k] == 0:
#         result.append(k)
#
# print(result)
#
# for row in result:
#     print(row,end=' ')

#-----------------------------------------------------------------------
#3
# arr = [[1,3,3,5,1],[3,6,2,4,2,],[1,9,2,6,5]]
# n = int(input())
# bucket = [0]*10
#
# for i in range(3):
#     for j in range(5):
#         bucket[arr[i][j]] +=1
#
# for i in range(len(bucket)):
#     if bucket[i] == n :
#         print(i,end=' ')


# print(bucket)

#------------------------------------------------------------------------------
#4
# cardlist=list(input())
# bucket = [0]*100
# result = []
#
# for i in range(len(cardlist)):
#     bucket[ord(cardlist[i])] += 1
#
# for i in range(len(bucket)):
#     if bucket[i] != 0 :
#         result.append(i)
#
# print(f"{len(result)}개")

#---------------------------------------------------------------------------------------
#5
# arr=list(input())
# bucket = [0]*100
#
# for i in range(len(arr)):
#     bucket[ord(arr[i])] += 1
#
# Max = -100000
# idx = 0
#
# for i in range(len(bucket)):
#     if Max<bucket[i]:
#         Max = bucket[i]
#         idx = i
#
# print(chr(idx))

#-------------------------------------------------------------------------------------
#6
# town = [["C","D","A"],["B","M","Z"],["Q","P","O"]]
# black = list(input())
# # print(black)
# bucket = [0] * 100
#
# for i in range(3):
#     for j in range(3):
#         bucket[ord(town[i][j])] += 1
#
# cnt =0
#
# for i in range(4):
#     if bucket[ord(black[i])] != 0:
#         cnt += 1
#
# print(f"{cnt}명")

#----------------------------------------------------------------------
#7
# arr = [["A","B","C"],["A","G","H"],["H","I","J"],["K","A","B"],["A","B","C"]]
# bucket = [0]*100
#
# for i in range(5):
#     for j in range(3):
#         bucket[ord(arr[i][j])] += 1
#
# lst = []
#
# for i in range(len(bucket)):
#     if bucket[i] != 0:
#         lst.append(chr(i)*bucket[i])
#
# for row in lst:
#     print(row,end='')

#-----------------------------------------------------------------------
#8
# train = [3,7,6,4,2,9,1,7]
# team = list(map(int,input().split()))
#
# idx = 0
#
# for i in range(8):
#     if idx != 0:
#         break
#     for j in range(3):
#         if train[i] != team[j]:
#             continue
#
#         if train[i] == team[j] :
#             idx = i
#             break
#
# print(f'{idx}번~{idx+2}번 칸')


# print(bucket)

#---------------------------------------------------------------------

#9
# apt = [[15,18,17],[4,6,9],[10,1,3],[7,8,9],[15,2,6]]
# family = list(map(int,input().split()))
#
#
# for i in range(5):
#     if apt[i][0] == family[0] and apt[i][1] == family[1] and apt[i][2] == family[2] :
#         print(f'{5-i}층')
#











































# for i in range(1,len(bucket)):
#     bucket[i]+=bucket[i-1]
#     # bucket[i]=bucket[i]+bucket[i-1]

# print(bucket)


#-------------------------------------------------------
# n=int(input())
# a=list(map(int,input().split()))
# # counting sort
#
# bucket=[0]*101
# # dat 등록
# for i in range(n):
#     bucket[a[i]]+=1
#
# # 누적합 구하기
# for i in range(1,len(bucket)):
#     bucket[i]+=bucket[i-1]
#     # bucket[i]=bucket[i]+bucket[i-1]
#
# # 값넣기
# result=[0]*101
# for i in range(n):
#     index=a[i]
#     result[bucket[index]-1]=a[i]
#     bucket[index]-=1
#
# for i in range(n):
#     print(result[i],end=' ')