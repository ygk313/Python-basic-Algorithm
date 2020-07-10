from collections import defaultdict

def count_sort(seq):
    b, c = [], defaultdict(list)
    for val in seq:
        c[val].append(val)
    
    for i in range(min(c), max(c)+1):
        b.extend(c[i])
    return b
    
if __name__=="__main__":
    seq = [3,5,2,6,8,1,0,3,5,6,2]

    print(count_sort(seq))