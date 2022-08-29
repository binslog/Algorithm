#1
n = int(input())
arr = [for _ in range(n)]

sort1 = sorted(arr, key=lambda x: (x[0], x[1]))
print(sort1)