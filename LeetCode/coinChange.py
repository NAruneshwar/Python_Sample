def coinChange(coins, amount):
    dp_array = [amount+1]*(amount+1)
    dp_array[0]=0
    for coin in coins:
        for i in range(amount+1):
            print(i//coin+dp_array[(i%coin)])
            dp_array[i]= min(i//coin+dp_array[(i%coin)],dp_array[i])
            
    print(dp_array)

coinChange([186,419,83,408],6249)
