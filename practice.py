from collections import deque

def solution(cards1, cards2, goal):
    deq1 = deque ()
    deq2 = deque ()
    
    # queue로 자료형태 바꾼다. 
    for card1 in cards1:
        deq1.append(card1)
    print(deq1)
    
    for card2 in cards2:
        deq2.append(card2)
    print(deq2)
    
    for word in goal:
        if word in deq1:
            deq1.popleft()
            break
        
        elif word in deq2:
            deq2.popleft()
            break
            
        elif len(deq1) == 0 or len(deq2) == 0 : return "Yes"
        
        else: return "No"



card1 = ["i", "drink", "water"]
card2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

answer = solution(card1, card2, goal)
print(answer)