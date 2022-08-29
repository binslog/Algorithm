T = int(input())
for k in range(T):
    num = int(input())
    arr = [[] for _ in range(num)]

    for i in range(0,num):
        arr[i] = (i+1)*[0]
    # print(arr)

    for i in range(num):
        for j in range(i+1):
            if i==0 or i == 1 :
                arr[i][j] = 1
            elif j == 0:
                arr[i][j] = 1
            elif i == j :
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j]+arr[i-1][j-1]

    print(f'#%d' %(k+1))
    for row in arr:
        print(*row)

