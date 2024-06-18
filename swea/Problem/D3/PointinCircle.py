#PointinCircle
TC= int(input())

for tc in range(TC):
    N = int(input())

    X,Y=N,N

    count=0
    for x in range(1,X+1,1):
        for y in range(Y+1):
            if(pow(x,2)+pow(y,2) <= pow(N,2)):
                count +=1
    count *=4
    count+=1

    print ("#"+str(tc+1  )+" "+str(count))