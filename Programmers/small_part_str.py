

def solution(keymap, targets):

  answer = [0] * len(targets)   

  for i in range(len(targets)):

      for j in range(len(list(targets[i]))):

          for k in range(len(keymap)):

              if list(keymap[k]).index("targets[j][i]") < cnt :
                  cnt = list(keymap[k]).index("targets[j][i]")
            
      answer[i] += cnt    
 

  return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
# print(list(targets[1]).index("B"))
result = solution(keymap,targets)
print(result)