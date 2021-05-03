def rec_sum(val):
    if len(val)<=1:
        return val[0]
    else:
        return val[0]+rec_sum(val[1:])

def num_of_items(val):
    if len(val)<=1:
        return 1
    else:
        return 1+num_of_items(val[1:])

def max_of_items(val):
    if len(val)<=1:
        return val[0]
    else:
        val2= max_of_items(val[1:])
        if val[0]<val2:
            return val2
        else:
            return val[0]



lis = [1,4,3,7,9,9,88,4,22]

# print(rec_sum(lis))

# print(num_of_items(lis))

print(max_of_items(lis))