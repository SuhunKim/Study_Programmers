T = int(input())

answer = []
for i in range(T):
    
    a,b = input().split()
    if(a>b):
        answer.append(">")
    elif(a==b):
        answer.append("=")
    else:
        answer.append("<")

for j in range(T):
    print("#{} {}".format(j+1, answer[j]))
