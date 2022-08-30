arr=['a','b','c']
path=['']*5


def abc(level):
    if level==2:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return

    for i in range(3):
        path[level]=arr[i]
        abc(level+1)
        path[level]=0

abc(0)








