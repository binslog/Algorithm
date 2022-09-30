# 15036 . 그래프 경로
# T=int(input())
#
# for tc in range(1,1+T):
#     v,e = map(int,input().split())
#     arr = [[] for _ in range(v + 1)]
#     for _ in range(e):
#         st, ed = map(int,input().split())
#         arr[st].append(ed)
#     start,end= map(int,input().split())
#     result=0
#     used=[0]*v+1
#
#     def dfs(now):
#         global result
#         if now == end:
#             result=1
#             return
#
#         for i in range(len(arr[now])):
#
#                 dfs(arr[now][i])
#
#     dfs(start)
#     print(f'#{tc} {result}')
# #
#

# --------------------------------------------------
# 13794 . 반복문자 지우기



# ---------------------------------------------------

# 13792. 종이붙이기


















# --------------------------------------------------
# 13789. 괄호검사
# T=int(input())
# for tc in range(1+T):
#     tests =list(input())
#     cnt1=0
#     cnt2=0
#
#     for test in tests:
#         if test == "{" :
#             cnt1 +=1
#         if test == "}":
#             cnt1 -=1
#
#         if test == "(":
#             cnt2 +=1
#         if test ==")":
#             cnt2 -=1
#
#     result=0
#     if cnt1 == 0 and cnt2 ==0 :
#         result=1
#     else:
#         result=0
#
#
#     print(f'#{tc} {result}')
#

# 델타배열
# dfs
# 최소신장트리, 크루스칼 알고리즘
