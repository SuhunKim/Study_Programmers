# from datetime import datetime

# T = int (input())

# days = [31,28,31,30,31,30,31,31,30,31,30,31]
# list_month = [1,2,3,4,5,6,7,8,9,10,11,12]

# list = []
# for i in range(T):
#     a=int(input())
#     year = a//10000
#     month = (a%10000)//100
#     day = (a%100)//1

#     if(0<month<13):
#         if(0<day<=days[month-1]):
#             dt = datetime(year,month,day)
#             str = dt.strftime("%4Y") +"/"+ dt.strftime("%m")+"/"+dt.strftime("%d")
#             list.append(str)
#         else:
#             list.append(-1)
#     else:
#         list.append(-1)
    
# for j in range(T):
#     print("#{} {}".format(j+1, list[j]))
	
T = int (input())

days = [31,28,31,30,31,30,31,31,30,31,30,31]
list_month = [1,2,3,4,5,6,7,8,9,10,11,12]

list = []
for i in range(T):
    a=int(input())
    year = a//10000
    month = (a%10000)//100
    day = (a%100)//1
    if(0<month<13):
        if(0<day<=days[month-1]):
            sYear = "{0:04d}/".format(year)
            sMonth ="{0:02d}/".format(month)
            sDay = "{0:02d}".format(day)
            sDate = sYear+sMonth+sDay
            list.append(sDate)

        else:
            list.append(-1)
    else:
        list.append(-1)
    
for j in range(T):
    print("#{} {}".format(j+1, list[j]))
	