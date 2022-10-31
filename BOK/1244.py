n=int(input())
Max=0

for i in range(n-1,-1,-1):
    lst = []
    lst.append(n)
    lst.append(i)
    now=2

    while lst[-1]>=0:
        new=lst[now-2]-lst[now-1]
        lst.append(new)
        now +=1

    if len(lst) > Max:
        Max = len(lst)
        result = lst

result.pop()
cnt=Max-1

print(cnt)
print(*result)
