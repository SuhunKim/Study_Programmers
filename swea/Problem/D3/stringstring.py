#stringstring

TC = int(input())

for tc in range(TC):
    N = int(input())
    S = input()

    lenS=len(S)
    answer=""
    if( lenS%2==0):
        half = int(lenS/2)
        a = S[0:half]
        b = S[half:lenS]
        if a==b:
            answer="Yes"
        else:
            answer="No"
    else:
        answer="No"

    print("#"+str(tc+1)+" "+answer)