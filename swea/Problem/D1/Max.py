T = int(input())

max = []
for i in range(T):
    list_num = list(map(int,input().split()))
    large=0
    for j in range(len(list_num)):
        if(large>list_num[j]):
            continue
        elif(large<list_num[j]):
            large=list_num[j]
        
    max.append(large)

for j in range(T):
    print("#{} {}".format(j+1,max[j]))
