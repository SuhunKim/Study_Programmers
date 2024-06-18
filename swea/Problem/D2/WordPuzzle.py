T = int (input())

for i in range (T   ):
    N,K = map(int, input().split())
    answer = 0
    square = []

    for _ in range(N):
        a = list(map(int, input().split()))
        square.append(a)

    # 검사식 구현 시작
    #   가로 검사
    count = 0
    for row in range(N):
        count=0
        for col in range(N):
            if(square[row][col] == 0):
                if(count==K):
                    answer+=1
                count=0
            else:
                count+=1
            

            if(count ==K and col==N-1):
                answer+=1
                count =0
    
    for col in range(N):
        count=0
        for row in range(N):
            if(square[row][col] == 0):
                if(count==K):
                    answer+=1
                count=0
            else:
                count+=1

            if(count ==K and row==N-1):
                answer+=1
                count=0
                 


    #   세로 검사

    print("#"+str( i+1)+" "+str(answer))