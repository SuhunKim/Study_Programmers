#codetree test 4
n = int(input())


a=2**n

list_answer=[]
listn=[]

for i in range(a):
    st = str(format(int(i),'b').zfill(4))
    before='0'
    count=0
    for char in range(4):
        if st[char] == before:
            before=st[char]
            count+=1

            
        else:
            count=0
        
    if(count==3):
            break
    else:
            list_answer.append(st)

for i in range(len(list_answer)):
    print(list_answer)