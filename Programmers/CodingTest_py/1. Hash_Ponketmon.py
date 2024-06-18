#N마리중 N/2마리 가져가기
#종류 별 번호로 구분
# N마리중 N/2 마리를 가져갈 때, 종류 수의 최댓값

def solution(nums):
    answer = 0
    numset = set()
    for i in nums:  # -> Set(nums) 하면 numset 끝
        numset.add(i)

    keycount = len(numset)
    totalcount = round(len(nums)/2)
    if totalcount<keycount:
        answer = totalcount
    
    else:
        answer=keycount
    
    

    return answer

ans = solution([3,1,2,3])
print(ans)


