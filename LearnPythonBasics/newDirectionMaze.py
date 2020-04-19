
def newpath(direction,i):
    result = ''
    for k in direction:
        if(k=="S"):
            result = str(result)+"E"
        elif(k=="E"):
            result= str(result)+"S"
    print("Case #%d: %s"%(i+1,result))
   
    return()


count = int(input())
for i in range(count):
    size = int(input())
    direction = input()
    newpath(direction,i)