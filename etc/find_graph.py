def bfs_graph(dic,start):
    qu =[]
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in dic[p]:
            if x not in done:
                qu.append(x)
                done.add(x)


def dfs_graph(dic,start):
    qu=[]
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in dic[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
            for y in dic[x]:
                if y not in done:
                    qu.append(y)
                    done.add(y)

dic = {'A':['B','C'],
        'B':['D','E'],
        'C':['A'],
        'D':['B'],
        'E':['B']}

bfs_graph(dic, 'A')
dfs_graph(dic,'A')
