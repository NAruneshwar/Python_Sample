def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n ==1:
        print (source,dest)
        return
    towerofhanoi(n-1,source,dest,aux)
    print(source,dest)
    towerofhanoi(n-1,aux,source,dest)

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')