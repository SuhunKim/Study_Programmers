#arithmetic sequence

TC = int(input())



for tc in range(TC):
    answer = 0
    a,b,c = map(int,input().split())
    ab = abs( a-b)
    bc =abs( b-c)
    ac = abs(a-c)


    if ab==bc:
        answer=0.0
    else:
        answer =  round(min([abs(a - ((2*b)-c)), abs(b-((a+c)/2)), abs(c - ((2*b)-a))]), 1)#round(min(abs(a-((2*b)-c)), abs(b-((a+c)/2)), abs(c-((2*b)-a))),1)
        # answer = round(min([abs(a - ((2*b)-c)), abs(b-((a+c)/2)), abs(c - ((2*b)-a))]), 1)
    
    print("#"+str(tc+1)+" "+str(answer)) if not answer==0.0 else print("#"+str(tc+1)+" 0.0") #+str(answer)) 