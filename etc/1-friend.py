def print_all_Friends(g,s):
    qu = []
    done = set()

    qu.append(s)
    done.add(s)

    while qu:
        p = qu.pop(0)
        print(p)
        if p in g.keys():
            for x in g[p]:
                if x not in done:
                    qu.append(x)
                    done.add(x)

fr_info={
        'summer':['John','Justin','Mike'],
        'John':['summer','Justin'],
        'Justin':['John','Summer','Mike','May']}

print_all_Friends(fr_info, 'summer')
