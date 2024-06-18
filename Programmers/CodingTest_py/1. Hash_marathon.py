#marathon.py

#참여자 participant
#완주자  completion
#미완주 answer

# 효율성 문제 해결 못함

# def solution(participant, completion):
#     a = list(participant)

#     for i in completion:
#         a.remove(i)

#     return a[0]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]