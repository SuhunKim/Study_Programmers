T = int(input())

list_len = []


for i in range (T):
    answer=0
    check=[]
    arr = str(input())
    first = arr[0]

    for j in arr:
        if j not in check:
             check.append(j)
             answer +=1
        else :
            check.pop(check.index(j))
            answer +=1

        if not check:
            answer = answer//2
            list_len.append(str(answer))
            break
    
for time in range(T):
    print("#"+str(time+1)+" "+list_len[time])

