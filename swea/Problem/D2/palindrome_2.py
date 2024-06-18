T = int(input())


for i in range(T):
    org = str(input())
    obj = ""
    leng = len(org)
    middle = (leng//2) +1
    # check=[]
    bAnswer = False
    index = 0
    for j in range(middle):
        obj+=org[j]
        index = j
    
    for j in range(middle,leng,1):
        index -=1
        if(org[index]==org[j]):
            obj+=org[j]
        else:
            break 

    if(obj == org):
        bAnswer = True

    print("#"+str(i+1)+" {0}".format("1" if bAnswer else "0"))