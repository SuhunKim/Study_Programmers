#Aver of Aver
T= int(input())

for t in range(T):
    N = int(input())
    S = list(map(int,input().split()))

    
    answer = round(sum(S)/N)  if sum(S)%N == 0 else round(sum(S)/N,20)
    print("#"+str(t+1)+" "+str( answer ))