# 5566. 주사위게임(bronze2)
n,m=map(int,input().split())
arr=[]
dice=[]

# 배열에 주어진 값 넣는다.
for _ in range(n):
    x=int(input())
    arr.append(x)

for _ in range(m):
    y=int(input())
    dice.append(y)

result=0
now=0

# 현재 위치를 now로 설정하고 now가 n이 될때까지..!
for i in range(m):
    now += dice[i] # 1. 먼저 주사위 움직이고
    if now >= n or i == m-1 : # 주의!! i == m-1이 없으면 마지막에 도달했을 때를 카운트 못한다.
        result=i+1
        break
    else:
        now += arr[now] # 2. 판에 움직인 만큼 간다.
        if now >= n or i == m-1 : # 조건을 여기에도 걸어주어야 한다.
            result=i+1
            break

print(result)

