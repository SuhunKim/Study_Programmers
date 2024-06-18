TC = int(input ())

for tc in range(TC):
    ij = int (input())
    dest = round(ij**(1/2))

    list_div=[]
    answer=0
    
    for i in range(1,dest+1,1):
        if(ij%i==0) :
            list_div.append((i-1)+(ij//i)-1)


    # for i in range(1,dest+1,1):
    #     if(ij%i==0) :
    #         list_div.append(int(i))
    #         list_div.append(int(ij//i))

    # list_div.sort()
    # length = len(list_div)
    # if(length==2):
    #     a=list_div[0]
    #     b=list_div[1]
    #     answer= a+b-2

    # else:
    #     a=list_div[(length//2)]
    #     b=list_div[(length//2)-1]
    #     answer= a+b-2

    print("#"+str(tc+1)+" "+str(min(list_div)))