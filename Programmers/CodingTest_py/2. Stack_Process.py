def solution(priorities, location):
    answer = 0
    
    d_index = {}
    for i in priorities:    #dict  활용 가능?
        d_index[i] = priorities[i]    
    
    start = priorities.index(max(priorities))
    new = []
    # for i in range(start,len(priorities),1):
    #     new.append(priorities[i])
    for i in priorities[start:len(priorities)]:
        new.append(i)
    
    # new2 = priorities[start:-start]




    seq = 1
    while max(priorities)>0:
        m = priorities.index(max(priorities))
        d_index[m] = seq
        seq+=1
        priorities[m]=0
        
        
    
        
    answer=d_index[location]
    return answer-start


print(solution([2, 1, 3, 2]	,2))    # 3 4 1 2 순서 중 index 2-> 3 의 순서 1 return 1