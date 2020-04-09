def binary_search(a,x):
    start = 0
    end = len(a)-1
    while end>=start:
        mid = (start+end)//2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid+1
        elif x < a[mid]:
            end = mid-1
    return -1

a = [1,3,4,5,6]
print(binary_search(a,4))

