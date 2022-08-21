# insert selection
# a = [8,3,1,5,7,10]
#
# result = []
# for i in range(len(a)):
#     result.append(a[i])
#     for j in range(i,0,-1):
#         if result[j-1]>result[j]:
#             result[j-1],result[j]=result[j],result[j-1]
#
# print(result)

#-------------------------------------------------------------------------
# 해당 패턴이 몇 개 있는가?
# n,m = map(int,(input().split()))
# arr = [list(map(int,input().split())) for _ in range(n)]
# pt = [list(map(int,input().split())) for _ in range(2)]
#
# # dx = [-1,1,0,0]
# # dy = [0,0,-1,1]
# cnt=0
#
# def findpattern(y,x):
#
#     for i in range(2):
#         for j in range(2):
#             if pt[i][j] != arr[y+i][x+j]:
#                 return 0
#         return 1
#
#
# for i in range(2):
#     for j in range(2):
#         cnt += findpattern(i,j)
#
#
#
# print(f'{cnt}개 있습니다.')

#-------------------------------------------------------------------

# 상 하 좌 우 합 구하기

# arr=[[3,5,4],[1,1,2],[1,3,9]]
# y,x=map(int,input().split())
#
# directx = [-1,1,0,0]
# directy = [0,0,-1,1]
# sum = 0
#
# for i in range(4):
#         dy = directy[i] + y
#         dx = directx[i] + x
#
#         if dy < 0 or dx < 0 or dy > 2 or dy > 2:
#             continue
#         else:
#             sum += arr[dy][dx]
#
# print(sum)

#----------------------------------------------------------------------------

# 이진검색

# def binarysearch(a,n,key):
#     start = 0
#     end = n-1
#     while start <= end :
#         middle = (start+end) //2
#         if a[middle] ==key
#             return true
#         elif a[middle] > key:
#             end = middle -1
#         else:
#             start = middle +1
#     return false
#
# call_binary = binarysearch(5,10,7)
# print(call_binary)


#-------------------------------------------------------------------
# selection algorithm
arr=[3,4,5,7,9,2]

def select(arr,k):
    for i in range(0,k):
        minindex = i
        for j in range(i+1,len(arr)):
            if arr[minindex]> arr[j]:
                minindex = j

        arr[j],arr[minindex] = arr[minindex],arr[j]

    return arr[k-1]

call_select = select(arr,6)
print(call_select)















