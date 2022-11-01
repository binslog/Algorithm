n1 = int(input())
arr = list(map(int,input().split()))

n2 = int(input())
lst = [[0] * 2 for _ in range(n2)]
for i in range(n2):
    lst[i][0],lst[i][1] = map(int,input().split())

# print(lst)
for i in range(n2):
    if lst[i][0] == 1:
        for j in range(lst[i][1],n2):
            if j == lst[i][1]

