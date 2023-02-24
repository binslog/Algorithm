def solution (s,skip,index):
    answer =""
    idx=0
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for ch1 in skip:
        if ch1 in alphabet:
            alphabet = alphabet.replace(ch1,"")
    print(alphabet)

    for ch2 in s :
        idx = (alphabet.index(ch2) + index) % len(alphabet)

        print(alphabet.index(ch2), idx)

        answer += alphabet[idx]

    return answer

s,skip,index = 'aukks','wbqd',5
res = solution(s,skip,index)
print(res)