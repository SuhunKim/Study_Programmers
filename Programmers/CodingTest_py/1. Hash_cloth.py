#매일 다른 조합, 서로다른 조합의 수


# def solution(clothes):
#     answer = 1
#     count = len(clothes)    
#     list_cnt=[]

#     for i in range(count):
# #        list_cnt.append(len(clothes[i]))
#         answer *=len(clothes[i])

def solution(clothes):
    answer = 1
    count = len(clothes)    

    hash = {}
    type = set()
    for i in range(count): #== for i in count:
        type.add(clothes[i][1]) #type 개수 

        if hash.get(clothes[i][1]) is None:
            hash[clothes[i][1]]=[clothes[i][0]]
        else:
            hash[clothes[i][1]].append(clothes[i][0]) # 타입별 개수

    # if len(hash) != 1:
    for i in hash:
        
        answer *= (len(hash[i])+1)

    # answer+=count

    # print(answer)
    return answer-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])