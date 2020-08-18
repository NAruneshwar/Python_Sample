

def distributeCandies(candies, num_people):

    result = [0]*num_people
    for k in range(1,candies+1):
        if candies>k:
            result[k%num_people]+=k
            candies-=k
        else:
            result[k%num_people]+=candies
            result.append(result[0])
            result.pop(0)
            return(result)
    return(result)





print(distributeCandies(7,4))