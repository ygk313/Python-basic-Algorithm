def bubble_sort(seq):
    length = len(seq)-1
    for num in range(length, 0, -1):
        for j in range(num):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
    
    return seq


if __name__=="__main__":
    seq = [11,3,28,43,9,4]
    print(bubble_sort(seq))