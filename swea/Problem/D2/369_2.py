T = int ( input())

list_result = []

for i in range(1,T+1,1):
    answer =""

    a=i//100
    b=i%100//10
    c=i%10//1

    if(a==3 or a==6 or a==9):
        answer +="-"
    if(b==3 or b==6 or b==9):
        answer +="-"
    if(c==3 or c==6 or c==9):
        answer +="-"
    
    if  "-" not in answer:
        answer = str(i)


    list_result.append(answer)

print(' '.join(list_result)) 