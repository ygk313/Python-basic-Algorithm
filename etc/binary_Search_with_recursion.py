def recursion_bi(a,start,end,x):
    #이거는 찾는 대상이 없을 떄 실행할 문장
    if start > end:
        return -1
    
    mid = (start+end)//2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return recursion_bi(a,mid+1, end, x)
    elif x < a[mid]:
        return recursion_bi(a, start, mid-1, x)
    return -1

a =[1,2,3,4]
print(recursion_bi(a, 0, len(a)-1, 2))
print(recursion_bi(a, 0, len(a)-1, 6))

