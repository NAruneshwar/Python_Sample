def mergeSort(arr,l,r):
    if r<l:
        m = (l+r)//2
        a1 = mergeSort(arr,l,m)
        a2 = mergeSort(arr,m+1,r)
        merge(arr, a1, a2)
    else:
        return 
    return arr



def merge(arr, a1, a2):
    l,m = 0,0
    while l<len(a1) and m<len(a2):
        if arr[l]<=arr[m]:
            
        elif:


    return