T = int(input())


for i in range(T):
    list_ten = list(map(int, input().split()))
    

    middle= sum(list_ten) - max(list_ten)-min(list_ten)
    result = round((middle/8))
    

    print("#"+str(i+1)+" "+str(result)) #(len(list_ten)-2)))