T=int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0 # 봉우리 개수

    # 봉우리가 1개인 경우 따로 빼주자. index 오류 방지
    if len(arr)==1:
        cnt=1

    # 지형이 모두 같은 경우의 수를 따로 빼주자.
    if len(set(arr)) == 1:
        cnt = 1

    # 나머지 경우
    else:
        # 맨 앞은 다음보다 크면 봉우리로 인식한다.
        if arr[0] > arr[1] :
            cnt += 1

        # 맨 뒤쪽 지형은 이전보다 높으면 봉우리로 인식한다.
        if arr[-1] > arr[-2]:
            cnt += 1

        # 나머지 봉우리 세준다.
        for i in range(1,n-1):
            if arr[i+1] > arr[i]: # 뒤의 봉우리가 앞 봉우리보다 크다면,
                for j in range(i+1,n-1): # 다시 for문 들어가서,
                    if arr[j+1] < arr[j]: # 앞 봉우리가 커지는 순간 카운트하고 나온다.
                        cnt+=1
                        break

                    if arr[j+1] > arr[j]: # 그 뒤 봉우리가 크다면 의미 없음
                        break


    # 만일 모든 조건을 충족하지 않는다고 하더라도, 봉우리가 0인 경우는 없다.
    if cnt == 0:
        cnt=1

    print(f'#{tc} {cnt}')