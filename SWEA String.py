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
















