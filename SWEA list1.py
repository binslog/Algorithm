# 13569 gravity
# T = int(input())
# for tc in range(T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     Max = 0
#     for i in range(len(arr)-1):
#         cnt = 0
#         for j in range(i+1,len(arr)):
#             if arr[i] > arr[j]:
#                 cnt += 1
#         if cnt > Max:
#             Max = cnt
#     print(f"#{tc} {Max}")
#


# -----------------------------------------------------------------
# 13568 구간합
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

# -------------------------------------------------------------------
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

#---------------------------------------------------------------------------
# 13565 전기버스
# T=int(input())
#
# for tc in range(1,T+1):
#     K,N,M = map(int,(input().split()))
#     stops = list(map(int,input().split()))
#
#     now=0
#     cnt=0
#     next=now+K
#
#     while next != N:
#         if next in stops:
#             now=next
#             next=now+K
#             cnt+=1
#         else:
#             next-=1
#         if next == now:
#             cnt = 0
#             break
#
#     print(f'#{tc} {cnt}')


#-----------------------------------------------------------
# 13564. min max
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     result = max(numbers) - min(numbers)
#
#     print(f'#{tc} {result}')



