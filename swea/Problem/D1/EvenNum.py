# T = int(input())

# list_answer = []

# for _ in range(T):
#     line_answer = 0
#     list_odd = []
#     A = map(int,input().split(' '))

#     for a in A:
#         if(a%2==1):
#             {
#                 list_odd.append(a)
#             }

# for i in list_odd:
#     line_answer = line_answer + i

# list_answer.append(line_answer)

# for j in list_answer:
#     print(j)

T=int(input())
list_answer = []
for i in range(T):
    result=0
    data=list(map(int,input().split()))
    for j in range(len(data)):
        if data[j]%2 == 1:
            result+=data[j]
    list_answer.append(result)

i=0
for j in list_answer:
    print("#",i," ",j)
    i=i+1