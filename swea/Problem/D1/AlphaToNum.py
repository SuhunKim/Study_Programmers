T = str(input())

list_T = list(T)

len = len(list_T)

list_Num = []

for i in list_T:
    list_Num.append(str(ord(i)-64))

print(' '.join(list_Num))
