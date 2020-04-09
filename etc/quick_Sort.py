def partition(list, start, end):
    pivot = start
    low = start
    high = end
    while low<high:
        while low<=end and list[low]<list[pivot]:
            low+=1
        while high>=start and list[high]>list[pivot]:
            high-=1
        if (high>low):
            list[low],list[high] = list[high], list[low]

    list[high],list[pivot] = list[pivot],list[high]
    return high

def quick_sort(list, start, end):
    if (end>start):
        q = partition(list, start, end)
        quick_sort(list, start, q-1)
        quick_sort(list, q+1, end)

list=[6,8,3,9,10,1,2,4,7,5]
quick_sort(list,0,len(list)-1)
print(list)
