
def mergeSort(arr):
    # Please add your code here
    if len(arr)==0 or len(arr)==1:
        return 
    mid = len(arr)//2
    a1 = arr[:mid]
    a2 = arr[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(arr,a1,a2)


def merge(arr,lis1,lis2):
    a=0
    b= 0
    k = 0
    while(a<len(lis1) and b<len(lis2)):
        if lis1[a]<lis2[b]:
            arr[k] = lis1[a]
            a+=1
            k+=1
        else:
            arr[k] = lis2[b]
            b+=1
            k+=1
    while(a<len(lis1)):
        arr[k] = lis1[a]
        a+=1
        k+=1
    while(b<len(lis2)):
            arr[k] = lis2[b]
            b+=1
            k+=1
    return 
    
            

lis = [1,4,3,7,9,9,88,4,22]
(mergeSort(lis))
print(lis)