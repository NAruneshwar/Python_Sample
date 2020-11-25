from collections import defaultdict
def carPooling( trips, capacity):
    line = defaultdict(int)
    for each in trips:
        for i in range(each[1],each[2]):
            line[i]+=each[0]
            if line[i]>capacity:
                return False

    return True



print(carPooling([[2,1,50000],[3,3,7]], 4))