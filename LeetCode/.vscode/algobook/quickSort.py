def quick_sort(lis):
    if len(lis)<2:
        return lis
    else:
        pivot = lis[0]
        count = lis.count(pivot)
        less = [a for a in lis if a<pivot]
        more = [a for a in lis if a>pivot]
        return quick_sort(less) + [pivot]*count + quick_sort(more)


lis = [1,1,4,3,7,9,9,88,4,22]
print(quick_sort(lis))