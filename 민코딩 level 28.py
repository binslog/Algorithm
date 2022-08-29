#1
# name = ["Amy","Edger","Bob","Diane","Chloe"]
#
# arr = [[0,1,0,0,0],
#        [0,0,0,0,0],
#        [1,0,0,0,0],
#        [0,0,1,0,0],
#        [0,0,1,0,0]]
#
# sum = 0
# max = 0
# maxindex = 0
#
#
# for j in range(5):
#     sum=0
#     for i in range(5):
#         if arr[i][j] == 1:
#             sum += 1
#
#         if sum > max :
#             max = sum
#             maxindex =j
#
# print(name[maxindex])

#-----------------------------------------------------------
#2
num = int(input())
arr = [list(map(int,input().split())) for _ in range(num)]


boss_index = []
under_index = []



for j in range(num):
    for i in range(num):
        if j==0 and arr[i][j] == 1:
            boss_index.append(i)

boss_index = ' '.join(str(s) for s in boss_index)

print(f'boss:{boss_index}')

def dfs(now):
    for k in range(num):
        if arr[now][k] == 1 :
            under_index.append(k)
            dfs(k)
dfs(0)

under_result = ' '.join(str(s) for s in under_index)
print(f"under:{under_result}")


# high_index = ' '.join(str(s) for s in high_index)
#
