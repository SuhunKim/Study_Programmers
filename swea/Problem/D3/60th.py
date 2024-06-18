TC = int(input())

for tc in range(TC):
    N,M = map(int,input().split())  #N x M

    list_n = list(map(str,input().split()))     #List N
    list_m = list(map(str,input().split()))     #List M

    reps = int(input())
    list_Answer = []
    for rep in range(reps):
        year = int(input())
        
        nNum = N-1 if year%N==0 else (year%N)-1
        mNum = M-1 if year%M==0 else (year%M)-1
        # mNum = year%M


        Name = "{0}{1}".format(list_n[nNum],list_m[mNum])

        list_Answer.append(Name)

    print("#"+str(tc+1)+' '+' '.join(list_Answer))

    