T= int(input())

for i in range(T):
    N = int(input())
    sum=0

    for n in range(1,N+1,1):
        if(n%2==0):
            sum-=n
        else:
            sum+=n   
    

    print("#"+str(i+1)+" "+str(sum))