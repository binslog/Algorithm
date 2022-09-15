# 1
# arr = [4,4,5,7,8,10,20,22,23,24]
# target = int(input())
#
# def binary_search(st,ed,value):
#     while 1:
#         mid = (st+ed)//2
#         if arr[mid] == value:
#             return 1
#         elif arr[mid] > value:
#             ed = mid-1
#         elif arr[mid] < value:
#             st = mid+1
#         if st>ed:
#             return 0
#
# ret=binary_search(0,len(arr)-1,target)
#
# if ret:
#     print("O")
# else:
#     print("X")

# -------------------------------------------------
# 2
# bettery=list(input())
# def parametric_search(st,ed):
#     Max=-1
#     while (1):
#         mid=(st+ed)//2
#         if bettery[mid]=='_':
#             ed=mid-1
#         elif bettery[mid]=='#':
#             Max=mid
#             st=mid+1
#         if st>ed:
#             break
#     return Max+1
#
#
# answer=parametric_search(0,9)
# print(f'{answer*10}%')

# -----------------------------------------------------













# -------------------------------------------------------
# 4
# n = int(input())
# curser = [list(input()) for _ in range(n)]
#
# def bs1(st,ed):
#     Max=-1
#     while(1):
#         mid=(st+ed)//2
#         if curser[mid][0]=='0':
#             ed=mid-1
#         elif curser[mid][0]=='#':
#             Max=mid
#             st=mid+1
#         if st>ed:
#             break
#
#     return Max+1
#
# ret=bs1(0,len(curser)-1)
# print(ret)














