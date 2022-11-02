# 버블탐색 하면 시간 초과..!!

# n,t = map(int,input().split())
# arr = list(map(int,input().split()))
#
# Max=-21e8
#
# for i in range(n-t+1):
#     Sum = 0
#     for j in range(i,i+t):
#         Sum += arr[j]
#
#     if Max < Sum :
#         Max = Sum
#
# print(Max)

# -----------------------------------------------

# 슬라이딩 윈도우 해주자
# def minSlidingWindow(nums,t,k):
#     Max_sum = -21e8
#     window_sum = 0
#     start = 0
#
#     for end in range(t):
#         window_sum += nums[end]
#
#         if end >= k - 1:
#             # 0~k-1 까지 더한 값이 최소값보다 작다면, 최소값을 갱신
#             if window_sum >= Max_sum:
#                 Max_sum= window_sum
#
#             # 윈도우에 포함된 맨 앞자리 수를 제거
#             window_sum -= nums[start]
#             # 윈도우 시작 인덱스를 하나 증가
#             start += 1
#
#     return Max_sum
#
#
# t,k = map(int,input().split())
# nums = list(map(int,input().split()))
# ret=minSlidingWindow(nums,t,k)
# print(ret)


# -----------------------------------------------------



