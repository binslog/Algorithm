def solution(numbers):
    stack = [] # numbers의 원소의 인덱스들이 들어간다.
    answer = [0] * len(numbers)

    for i in range(len(numbers)):
        # stack의 마지막 인덱스의 value와 numbers[i] 값과 비교하여 pop
        while stack and numbers[stack[-1]] < numbers[i]:  
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    # stack에 남아있는 인덱스들은 뒤 큰 수가 없는 원소들이니까 -1로 채운다.
    while stack:
        answer[stack.pop()] = -1
      
    return answer


