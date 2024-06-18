from itertools import permutations

def solution(numbers):
    answer=0
    alist=[] 
    for i in range(len(numbers)):
        alist.append(numbers[i])

    a=set()

    for permu in permutations(alist,len(alist)):
        prime=0
        value = int(''.join(permu))
        
        if  value > 1:
            for i in range(1,value+1,1):
                if value%i==0:
                    prime+=1
            if prime==2:
                answer+=1
            a.add(value)



            
    return len(a)#set(answer))
        # alist.append(permu)

solution("17")