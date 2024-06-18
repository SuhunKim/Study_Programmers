TC = int(input())

for i in range(TC):
	N = int(input()) #품목 수 N
	list_print = list(map(int,input().split()))
	list_print.reverse()
	list_answer = []
	
	n=0
	while N<len(list_print) :
		if(round(list_print[n]*0.75) in list_print) :
			index = list_print.index(round(list_print[n]*0.75))
			temp = list_print.pop(index)

			list_answer.append(str(temp))
			n+=1
		
		else : 
			list_answer.append(str(n))
			list_print.pop(n)
		
	list_answer.reverse()
	print("#"+str(i+1)+" "+" ".join(list_answer))