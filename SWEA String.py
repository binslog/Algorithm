# 13761 가장 빠른 문자열 타이핑

# T=int(input())
# for tc in range(1,T+1):
#     A,B = input().split()
#     cnt_B=0
#
#     for i in range(len(A)-len(B)+1):
#         if A[i:i+len(B)] == B:
#             cnt_B +=1
#
#     result = len(A) - cnt_B*len(B) + cnt_B
#     print(f'#{tc} {result}')

# -------------------------------------------
# 13741 글자수

# T=int(input())
#
# for tc in range(1,T+1):
#     str1 = input()
#     str2 = input()
#     c_dict = {}
#
#     for a in str1:
#         if a not in c_dict:
#             c_dict[a] = 0
#
#     for a in str2:
#         if a in c_dict:
#            c_dict[a]+=1
#
#     result=max(c_dict.values())
#     print(f'#{tc} {result}')
#

# ------------------------------------------
# 13740 회문
# T=int(input())
#
# for tc in range(1,T+1):
#     N,M = map(int,(input().split()))
#     palin = [list(input()) for _ in range(N)]
#
#     flag=0
#     # 가로 검색
#     for i in range(N):
#         for j in range(N-M+1):
#             for k in range(M):
#                 if palin[i][j+k] == palin[i][N-k-1]:
#                     flag=1
#                 else:
#                     flag = 0
#                     break
#         if flag == 1:
#             result = palin[i][j:j+M]
#
#     # --------------------------------------------------
#
#
#     palin_r = [[0] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             palin_r[i][j] = palin[j][i]
#
#     # 세로 검색
#     flag=0
#     for i in range(N):
#         for j in range(N-M+1):
#             for k in range(M):
#                 if palin_r[i][j+k] == palin_r[i][N-k-1]:
#                     flag=1
#                 else:
#                     flag = 0
#                     break
#         if flag == 1:
#             result = palin_r[i][j:j+M]
#
#     print(f'#{tc}',end=' ')
#     print(*result,sep='')


# -----------------------------------------------------------------
# 13738 문자열 비교
# T = int(input())
#
# for tc in range(1,T+1):
#     str1=input()
#     str2=input()
#
#     result=0
#     for i in range(len(str2)-len(str1)+1):
#         if str2[i:i+len(str1)] == str1:
#             result +=1
#
#     print(f'#{tc} {result}')

# ------------------------------------------------------
# 1221 5일차-GNS
# T=int(input())
#
# for tc in range(1,T+1):
#     a = input().split()
#     num=a[0]
#     total=a[1]
#
#     numbers = list(input().split())
#     orders = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     result=[]
#
#     for i in range(10):
#         for j in range(len(numbers)):
#             if orders[i] == numbers[j]:
#                 result.append(numbers[j])
#
#     print(f'{num}')
#     print(*result)


# ---------------------------------------------------
# 1216. [S/W 문제해결 기본] 3일차 - 회문2
for tc in range(1,11):
    palin = [list(input()) for _ in range(100)]
    flag=0
    result=[]
    # 가로 검색
    for i in range(100):
        for j in range(100,0,-1):
            for k in range(j):
                if palin[i][k] == palin[i][99-k]:
                    flag=1
                else:
                    flag=0
                    break

            if flag == 1:
                result = palin[i][j:2*j]
                break

    # --------------------------------------------------


    palin_r = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            palin_r[i][j] = palin[j][i]
    #
    # # 세로 검색
    # flag=0
    # for i in range(N):
    #     for j in range(N-M+1):
    #         for k in range(M):
    #             if palin_r[i][j+k] == palin_r[i][N-k-1]:
    #                 flag=1
    #             else:
    #                 flag = 0
    #                 break
    #     if flag == 1:
    #         result = palin_r[i][j:j+M]
    #
    # print(f'#{tc}',end=' ')
    print(*result,sep='')















# ----------------------------------------------------------------------
# 1210. [S/W 문제해결 기본] 2일차 - Ladder1















# -------------------------------------------------------------------------


