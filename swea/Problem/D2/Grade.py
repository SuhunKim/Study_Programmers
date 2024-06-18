T = int (input())

list_grade = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]

for i in range(T):
    N,K = map(int,input().split())
    gradecount =N//10
    list_TotalScore = []

    for n in range(N):
        score = list(map(int,input().split ()))
        list_TotalScore.append(score[0]*0.35+score[1]*0.45+score[2]*0.2)
        

    sortScore = sorted(list_TotalScore,reverse=True)        
    key = sortScore.index(list_TotalScore[K-1])
    
    
    last_key = key//gradecount

    
    
    
    print("#"+str(i+1)+" "+list_grade[last_key])#str(last_key))
