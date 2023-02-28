today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

term=[]

# terms를 딕셔너리 형태로 바꾼다.
for i in range(len(terms)):
    term.append(terms[i].split(" "))
    
term_dic=dict(term)
# print(term_dic)


for i in range(len(privacies)):
    x= int(privacies[i][5:7]) + int(term_dic[privacies[i][-1]])
    print(x)
    # print(privacies[i][5:7])
    # privacies[i][5:7] = str(x)
        

# print(privacies)
