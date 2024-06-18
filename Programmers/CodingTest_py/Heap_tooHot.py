def solution(scoville, K):
    scoville.sort()

    answer = 0
    max=0

    for i in scoville:
        if i<K:
            scoville.append(scoville[0]+s[i]*2)
            scoville.sort()
            cnt+=1
        if s[0]>K:
            break
        # if len(s)==1 and s[0] <K:
        #     return -1
    return answer

solution([1, 2, 3, 9, 10, 12])