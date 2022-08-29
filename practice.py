
T = int(input())
for tc in range(1,T+1):
    N,minK,maxK = map(int,(input().split()))
    lst = list(map(int,input().split())) # 리스트 받고,
    scores=sorted(lst) # 원활한 진행을 위해서 정렬을 해준다.

    bucket = [0]*101
    for i in range(N):
        bucket[scores[i]] += 1

    # 반을 편성할 수 없을 경우 -1을 출력하기 위한 조작
    flag=0
    check=[]

    for i in range(len(bucket)):
        if bucket[i] != 0:
            check.append(bucket[i])

    for i in range(len(check)):
        if check[i] < minK:
            flag = 1

    cnt_list = sorted(check)

    # 반을 편성할 수 있다면 최소값을 산출해야 한다.

    result=0
    if len(set(cnt_list)) == 1:
        result = cnt_list[0]

    elif len(set(cnt_list)) == 2:
        result = cnt_list[1] - cnt_list[0]

    else:
        result = cnt_list[-1] - cnt_list[-2]



    if flag == 1:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {result}')


# 5 1 4
# 3 5 5 4 5
#
#
# 6 2 6
# 5 3 3 5 5 1


# 7 1 6
# 3 3 5 2 5 1 2

# 8 1 7
# 3 1 1 2 2 5 3 5
#
#
# 10 1 6
# 4 4 2 4 5 2 5 3 5 5




