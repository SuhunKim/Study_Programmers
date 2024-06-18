import math

TC = int(input())


for tc in range(TC):
    A,B = map(int,input().split())

    gcd=1

    if A==B:
        gcd=A
    else:
        gcd = 1

    print("#"+str(tc+1)+" "+str(gcd))