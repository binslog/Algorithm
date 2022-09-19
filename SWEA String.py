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

T=int(input())

for tc in range(1,T+1):
    str1,str2 = list(input()),list(input())
    bucket = [0]*101
    max_idx=0
    cnt=0

    for i in range(len(str1)):
        bucket[ord(str1[i])] += 1

    for i in range(101):
        if max(bucket)==bucket[i]:
            max_idx=i
            cnt+=1

    result=0
    for i in range(len(str2)):
        if max_idx == ord(str2[i]):
            result+=1


    print(f'#{tc} {result}')




# ------------------------------------------
# 13740 회문

















