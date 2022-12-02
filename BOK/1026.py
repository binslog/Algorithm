# 1026 보물(silver 4)
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
# print(A)
B_test=B[:]
# B를 움직였다면, 정렬을 통해서 하지만 안되기 때문에 얕은 복사를 하나 구현
# 그냥 복사하면 A,B 동시에 움직이는 깊은 복사가 된다.

lst=[0]*N
order=0

# 위치를 찾아주는 리스트를 만들고 -1을 대입하면서 index 리스트를 뽑아준다.
while sum(B_test) != -1 * N : # -1로 lst가 다 채워졌으면 끝.
    for i in range(N):
        if B_test[i] == max(B_test): # 최대값을 찾아서 index 값 넣어주고, 최대0 최소 n인 리스트 형성
            lst[i]=order
            B_test[i]=-1 # 넣어줬으면 -1로 최소로 만든다. 0이상 값 들어가니까
            order +=1
        if sum(B_test) == -1 * N : # 무한루프 방지
            break

Sum=0
for i in range(N):
    Sum+=A[lst[i]]*B[i] # A에서 index위치에 해당하는 값 찾아준다.

print(Sum)


# 최소와 최대를 이용한 풀이

# n = int(input())
#
# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))
#
# s = 0
# for i in range(n):
#     s += min(a_list) * max(b_list)
#     a_list.pop(a_list.index(min(a_list)))
#     b_list.pop(b_list.index(max(b_list)))
#
# print(s)