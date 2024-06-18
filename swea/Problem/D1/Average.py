T = int(input())

list_aver = []

for i in range(T):
    sum = 0
    arr =list(map(int, input().split())) 
#    n = len(arr)
    
    for j in range(len(arr)):
        sum+=arr[j]
    list_aver.append( round(sum/10))

for k in range(T):
    print("#{} {}".format(k+1,list_aver[k]))