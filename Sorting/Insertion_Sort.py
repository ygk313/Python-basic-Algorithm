def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j>0 and seq[j]<seq[j-1]:
            seq[j], seq[j-1] = seq[j-1], seq[j]
            j-=1
        
    return seq


if __name__=="__main__":
    seq = [3,5,2,6,8,1,0,3,5,6,2]

    print(insertion_sort(seq))