#Ladder1.py
TC =10
for tc in range(TC):
    num = int(input())
    # list_ladder = []
    # for i in range(100):
    #     list_ladder.append( list(map(int,input().split())))

    list_ladder = [list(map(int,input().split())) for _ in range(100)]

    X = list_ladder[99].index(2)

    for i in range(99,0,-1):

        # if(list_ladder[i-1][X] == 1):
        #     continue
        
        
        if list_ladder[i][X-1]==1 and X>0:
            while list_ladder[i][X-1]==1 and X>0:
                X-=1

            continue
        elif list_ladder[i][X+1]==1 and X<99:
            while list_ladder[i][X+1]==1 and X<99:
                X+=1
            continue
        
        

    print("#"+str(tc+1)+" "+str(X))
