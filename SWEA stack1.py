# 15036 . 그래프 경로
# T=int(input())
#
# for tc in range(1,1+T):
#     v,e = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(e)]
#     st,ed= map(int,input().split())
#
#     arr2=[[0]*50 for _ in range(1000)]
#
#     for i in range(e):
#         arr2[arr[i][0]][arr[i][1]]=1
#
#     result=0
#     def dfs(now):
#         global result
#         if now == ed:
#             result=1
#             return
#
#         for i in range(7):
#             if arr2[now][i] == 1:
#                 # arr[now]=0
#                 dfs(i)
#
#     dfs(st)
#     print(f'#{tc} {result}')

# --------------------------------------------------
# 13794 . 반복문자 지우기

word=list(input())

while 1:
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            del word[i]
            word=

        if len(set(word)) ==len(word):
            break

print(word)

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

