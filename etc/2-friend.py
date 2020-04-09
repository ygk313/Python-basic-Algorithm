def find_all_friends(g,start):
    qu=[]
    done = set()

    qu.append((start,0))
    done.add(start)

    while qu:
        (p,d) = qu.pop(0)
        print(p,d)
        for x in g[p]:
            if x not in done:
                qu.append((x,d+1))
                done.add(x)


friend_info ={'summer':['John','Justin'],
              'John':['summer','Justin'],
              'Justin':['John']
              }

find_all_friends(friend_info, 'summer')
