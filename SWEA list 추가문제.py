# 13893. 주사위 굴리기


# --------------------------------------------------------
# 13748. 진기의 최고급 붕어빵
# T=int(input())
#
# for tc in range(1,T+1):
#     N,M,K = map(int,input().split())
#     members = list(map(int,input().split()))
#     members=sorted(members)
#
#     cnt=0
#     flag=0
#     for member in members:
#         if (member//M)*K  > cnt:
#             cnt+=1
#             flag=0
#         else:
#             flag=1
#             break
#
#     if flag:
#         print(f"#{tc} Impossible")
#     else:
#         print(f"#{tc} Possible")






# ---------------------------------------------------------
# 1979. 어디에 단어가 들어갈 수 있을까
N,M = map(int,(input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]

directy=[0,1]
directx=[1,0]

result = 0
cnt=0
for i in range(N):
    for j in range(N):
        dy = directy[0]
        dx = directx[0]

            cnt +=1

        if cnt == M:
            result += 1
            break

for j in range(N):
    if cnt == M :
        result +=1
    cnt = 0
    for i in range(N):
        if arr[i][j] == 1:
            cnt +=1

print(result)














# ---------------------------------------------------------
# 1210. [S/W 문제해결 기본] 2일차 - Ladder1






