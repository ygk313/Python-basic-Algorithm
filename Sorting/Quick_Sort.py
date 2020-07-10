def partition(seq, start, end):
    pivot = start
    left = start+1
    right = end
    done = False

    while not done:
        while left <= right and seq[left]<=seq[pivot]:
            left +=1
        while left <= right and seq[pivot]<seq[right]:
            right-=1
        
        if left>right:
            done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]
        print('+',seq)
    seq[start], seq[right] = seq[right], seq[start]
    print("-",seq)
    return right

def quick_sort(seq, start,end):
    if start < end:
        pivot = partition(seq, start, end)
        quick_sort(seq, start, pivot-1)
        quick_sort(seq, pivot+1, end)
        print(pivot,seq)
    
    return seq

if __name__=="__main__":
    seq = [3,5,6,8,1,0,3,5,6,2]
    print(seq)
    seq = quick_sort(seq, 0, len(seq)-1)
    print(seq)