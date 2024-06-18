#faitigue 피로도.py

# from itertools import permutations
import itertools
def solution(k, dungeons):
    answer =0

    legnth = len(dungeons)

    for perm in itertools.permutations(dungeons, legnth):
        hp=k
        count=0

        for pm in perm:
            if hp >= pm[0]:
                hp-= pm[1]
                count+=1
            
            if count >answer:
                answer=count
    return answer

print(solution(3,[[80,20],[50,40],[30,10]]))