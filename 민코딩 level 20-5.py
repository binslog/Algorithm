#1
# def bbq(level):
#     if level == 2:
#          return
#     bbq(level+1)

# bbq(0)

#--------------------------------
#2
# arrs = list(input())
# result = []
# # result.append(arrs[1:5])
# # print(result)
#
# for i in range(len(arrs)):
#     result.append(arrs[len(arrs)-1-i:len(arrs)])
#
# # 이중 리스트를 꺼내는 방법
# # for j in range(i+1)만큼 가는게 포인트.
# for i in range(len(result)):
#     for j in range(i+1):
#         print(result[i][j],end='')
#     print()

#--------------------------------
#3
# a = list(input())
# b = len(a)//2
#
# if a[0:b] == a[b:len(a)]:
#     print("동일한문장")
# else:
#     print("다른문장")

#--------------------------------------------
#4
arr1 = [list(map(int,input().split())) for _ in range(4)]
input()
arr2 = [list(map(int,input().split())) for _ in range(4)]

flag = 0

for i in range(4):
    for j in range(4):
        if arr1[i][j] == 1 and arr2[i][j]==1:
            flag = 1

if flag:
    print("걸리다")
else:
    print("걸리지않는다")



#--------------------------------
#5
# alpha=input()
#
# lst=[ord(alpha)-3,ord(alpha)-2,ord(alpha)-1,ord(alpha),ord(alpha)+1,ord(alpha)+2,ord(alpha)+3]
#
# # print(lst)
#
# for i in range(7):
#     if lst[i] < 65 :
#         lst[i] += 26
#     elif lst[i] > 90 :
#         lst[i] -= 26
#
# for row in lst:
#     print(chr(row),end='')

#--------------------------------------------------------------------------
#6
# arr = list(map(int,input().split()))
# # print(arr)
# # result = [[0]*7 for _ in range(4)]
# # print(result)
#
# for i in range(4):
#     for j in range(i+4):
#        print(arr[j],end=' ')
#     print()


#--------------------------------
#7
# arr = list(input())
#
# for i in range(len(arr)):
#     for j in range(i+1):
#        print(arr[j],end='')
#     print()

#--------------------------------
#8
# arr1 = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))
# result =[]
#
# for i in range(4):
#     if arr1[i]<arr2[i]:
#         result.append(arr1[i])
#         result.append(arr2[i])
#     else:
#         result.append(arr2[i])
#         result.append(arr1[i])
#
# result = sorted(result)
# print(*result)


#--------------------------------
#9
# arr = [[3,5,4,2,5],[3,3,3,2,1],[3,2,6,7,8],[9,1,1,3,2]]
# a,b = map(int,(input().split()))
# Max = -21e10
#
# def patternmax(y,x):
#     result=0
#     for i in range(a):
#         for j in range(b):
#             dy = y + i
#             dx = x + j
#             result += arr[dy][dx]
#     return result
#
#
# for i in range(5-a):
#     for j in range(6-b):
#         rtn = patternmax(i,j)
#         if rtn > Max :
#             Max=rtn
#             y=i
#             x=j
#
#
# print('(%d,%d)' % (y,x))

