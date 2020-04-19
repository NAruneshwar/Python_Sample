def testfunc():
    lowerB =int(input())
    upperB =int(input())
    NoOfGuesses = int(input())
    for j in range(NoOfGuesses):
        mid = (lowerB+upperB)/2
        print(mid)
        result=input()
        if(result=='CORRECT'):
            return()
        elif(result=='TOO_SMALL'):
            lowerB=mid
        elif(result=='TOO_BIG'):
            upperB=mid
        




TC= int(input())
for k in range(TC):
    testfunc()
    