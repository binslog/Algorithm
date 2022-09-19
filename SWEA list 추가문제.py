N,M,K = map(int,input().split())
members = list(map(int,input().split()))
time = M/K

flag=0
for i in range(N):
    if members[0] > time:
        flag=1

    S