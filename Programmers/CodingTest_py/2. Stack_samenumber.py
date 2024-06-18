# 내 답
def solution(arr):
    answer = []
    #a= set()
    a = []
    for i in range(len(arr)):
        #a.add(i)
        if arr[i] in a:
            if arr[i] == arr[i-1]:
                continue
            else:
                a.append(arr[i])

        else:
            a.append(arr[i])

    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print(a)
    return a
    

solution([1,1,3,3,0,1,1])

# # 정답
# def no_continuous(s):
#     # 함수를 완성하세요
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue                # 인덱스 -1 빈 리스트(배열) 이어도 에러 없음
#         a.append(i)
#     return a

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( no_continuous( "133303" ))

#맘에드는 답
#def no_continuous(s):
#    # 함수를 완성하세요
#   result = []
#    for c in s:
#        if len(result) == 0 or result[-1] != c:
#            result.append(c)
#
#    return result