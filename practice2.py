arr = 'ABCMDABKSSDABS'

cnt_ab = 0
for i in range(len(arr)-1):
    if arr[i:i+2] == 'AB':
        cnt_ab += 1

print(cnt_ab)