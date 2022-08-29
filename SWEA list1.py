#13564. min max
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     result = max(numbers) - min(numbers)
#
#     print(f'#{tc} {result}')

#--------------------------------------------------------------
# #13565. 전기버스
# # T = int(input())
#
# # for tc in range(1,T+1):
# K,N,M = map(int,(input().split()))
# # K는 최대 이동 정류장의 갯수
# # N은 정류장 수
# # M은 충전기의 개수
# # 다음 리스트는 충전기가 설치된 곳을 의미한다.
#
# K,N,M = map(int,(input().split()))
# numbers = list(map(int,input().split()))
#
# flag=0
# for i in range(1,len(numbers)):
#     if numbers[i] - numbers[i-1] > K:
#         flag=1
#
#
# now=0
# cnt=0
# for i in range(1,M):
#      if now < numbers[0]+K :
#         now += numbers[i]
#
#      else:
#         cnt += 1
#         now -= numbers[i]
#
# print(cnt)


#-----------------------------------------------------------
# 13566 숫자카드
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     numbers = list(map(int,input()))
#     bucket =[0] * 10
#
#     for i in range(len(numbers)):
#         bucket[numbers[i]] +=1 # DAT 설정
#
#     Max = -10000
#     Maxidx = 0
#
#     for j in range(10):
#             if bucket[j] >= Max:
#                 Max = bucket[j]
#                 Maxidx = j
#
#     print(f'#{tc} {Maxidx} {Max}')


#----------------------------------------------------------------------------------
# 구간합
#     print(f'#{tc} ')
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int,(input().split()))
#     numbers = list(map(int,input().split()))
#
#     Max = -21e8
#     Min = 21e8
#
#     for i in range(N-M+1):
#         Sum = 0
#         for j in range(i,i+M):
#             Sum += numbers[j]
#         if Max < Sum:
#             Max = Sum # Max를 뽑아낸다.
#
#         Sum=0
#         for j in range(i,i+M):
#             Sum += numbers[j]
#         if Min > Sum:
#             Min = Sum # Min를 뽑아낸다.
#
#     print(f'#{tc} {Max-Min}')













