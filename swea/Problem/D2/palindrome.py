T = int (input())

list_answer =[]

for i in range(1,T,1):
    sentence = str(input())
    leng = len(sentence)
    check=[]
    bAnswer = False
    middle = (leng//2) +1

    for j in range(leng):
        
        if j not in check:
             check.append(j)
        else:
            check.pop(check.index(j))

        if not check:
            list_answer.add("1")
            bAnswer=True
    
    if(bAnswer is False):
        list_answer.add("0")

    if(check.pop() is sentence[middle]):
        print("#"+str(i)+' '+"1")

