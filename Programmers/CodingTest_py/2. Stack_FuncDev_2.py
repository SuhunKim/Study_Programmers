def solution(progresses, speeds):   #배포순서대로 정렬된 (작업진도 배열, 작업별 개발속도 배열)
    #배포는 하루 한번, 각 배포별 몇 개 기능 배포되는 지 return 
    answer = []

    endtime= []
    publish= []

    for i in range(len(progresses)):
        todo = 100 - progresses[i]
        how_day = todo// speeds[i] + (1 if todo%speeds[i] !=0 else 0)
        endtime.append(how_day)

    #today 739 / 5 10 1 1 20 1
    count = 0
    temp=0
    days=0
    for j in endtime:
        if j >temp:
            if count!= 0:
                answer.append(count)
                count=1
                temp=j

            else:
                count +=1
                temp=j
        else :
            count +=1

        # if j == endtime[len(endtime)-1]:
        #     answer.append(count)

    answer.append(count)  

    return answer

solution([93, 30, 55]   , [1, 30, 5])


 #solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])

#	def solution(progresses, speeds):   #배포순서대로 정렬된 (작업진도 배열, 작업별 개발속도 배열)
#	    answer = []
#	
#	    count = 0
#	    day = 0
#	    #for i in range(len(progresses)):
#	    while len(progresses)>0:
#	        if( progresses[0]+ day*speeds[0]>=100 ):
#	            progresses.pop(0)
#	            speeds.pop(0)
#	            count +=1
#	
#	        else:
#	            if count >0:
#	                answer.append(count)
#	                count=0
#	            day+=1
#	
#	    answer.append(count)
#	    return answer
#	
#	solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])
