def quickSort(arr, start, end):
    # Please add your code here
    if start>=end:
        return
    else:
        pivot_index = pivot_ele(arr,start,end) 
        quickSort(arr,start,pivot_index-1)
        quickSort(arr,pivot_index+1,end)
    print(arr)


def pivot_ele(arr, start, end):
    if start>=end:
        return
    pivot = arr[start]
    lower = 0
    for i in range(start,end):
        if arr[i]<pivot:
            lower+=1

    lower = start+lower
    arr[start], arr[lower]= arr[lower], arr[start]
    startcopy, endcopy = start,end
    while(startcopy<endcopy):
        if arr[startcopy]<arr[lower]:
            startcopy+=1
        elif arr[endcopy]>=arr[lower]:
            endcopy-=1
        else:
            arr[startcopy],arr[endcopy] = arr[endcopy],arr[startcopy]
            startcopy+=1
            endcopy-=1

    return lower

                
a= [1,5,2,6,88,44,22]
quickSort(a,0,len(a)-1)
print(a)