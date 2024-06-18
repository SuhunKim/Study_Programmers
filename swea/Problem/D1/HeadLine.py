arrT = str(input())

List_HeadLine = []

for i in arrT:
    if(97<=ord(i)<=122):
        i = chr(ord(i)-32)
    List_HeadLine.append(i)

print(''.join(List_HeadLine))