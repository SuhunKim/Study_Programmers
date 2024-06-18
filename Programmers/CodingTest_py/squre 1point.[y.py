def solution(v):
    answer = []
    ax,ay=0,0

    for x,y,z in zip(v,v[1:],v[2:]):
        if x[0] == y[0]:
            ax=z[0]
        elif x[1]==y[1]:
            ay=z[1]
        
        if x[0]==z[0]:
            ax=y[0]
        elif x[1]==z[1]:
            ay=y[1]    
        
        if y[0]==z[0]:
            ax=x[0]
        elif y[1]==z[1]:
            ay=x[1]    
    
    answer = [ax,ay]
    return answer


print(solution([[1,4],[3,4],[3,10]]))