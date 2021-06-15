def selectStock(saving, CurrentValue, futureValue):
    dp = [0]*(saving+1)
    for k in range(0,len(CurrentValue)):
        profit = futureValue[k]- CurrentValue[k]
        weight = CurrentValue[k]
        for i in range(saving,weight,-1):
            # print(dp[i])
            dp[i] = max(dp[i], dp[i-weight]+ profit)
    print(dp)
    return dp[saving]


print(selectStock(7, [1,3,4,5], [2,7,9,12]))