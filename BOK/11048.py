n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)] # DP 하나 만들어준다. 메모이제이션 할 거니깐

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+arr[i-1][j-1] # 점화식 하나 만들어 준다.

print(dp[i][j])




