

def solution(s, skip, index):
    result = []

    for word in list(s) :
        word_cnt = ord(word)

        for i in range(1,index+1):            
            if word_cnt >= 122 : 
                word_cnt -= 26

            if chr(word_cnt+i) in list(skip) : 
                word_cnt += 1

        word_cnt += index
                            
        if word_cnt >= 122 : 
            word_cnt -= 26
            
        result.append(chr(word_cnt))
            
            
    # print(result)

    answer = ''.join(s for s in result)
    
    return answer

s = 'zzxas'
skip = 'wbqd'
index = 5

res = solution(s,skip,index)
print(res)