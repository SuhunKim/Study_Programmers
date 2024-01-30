T = int( input())


for Time in range(1,T+1,1):
    dic_arr = {}
    print("#"+str(Time))
    size = int(input())

    for i in range(1,size+1,1):
        ilist=[]
        slist = []
        if(i==1):
            slist.append("1")
            ilist.append(1)
        else:
            for j in range(i):
                if j==0:
                    ilist.append(1)
                    slist.append("1")
                elif j==i-1:
                    ilist.append(1)
                    slist.append("1")
                else:
                    ilist.append(dic_arr[i-1][j-1]+dic_arr[i-1][j])
                    slist.append(str(dic_arr[i-1][j-1]+dic_arr[i-1][j]))
        dic_arr[i]=ilist

        print(' '.join(slist))