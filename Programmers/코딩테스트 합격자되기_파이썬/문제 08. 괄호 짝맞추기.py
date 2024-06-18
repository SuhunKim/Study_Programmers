#닫힌 괄호가 임의 위치의 열린 괄호와 상쇄되는 것이 아니라
# 닫힌 괄호가 나오기 바로 전의, 
#즉, 가장 가까운(최근) 열린 괄호와 상쇄된다는 겁니다.

#1 문자열을 앞에서 하나씩 보며 열린 괄호가 나오면 푸시
#2 닫힌 괄호가 나오면 팝 연산을 통해 문자열에서 열린 괄호, 닫힌 괄호 한 쌍을 상쇄

# 1,2 반복,마지막문자열 이후 스택에 열린괄호가 남아있으면 X, 남은게 없으면  True

def solution(s):
    stack = []

    for c in s:
        if c =='(': #열린괄호 -> Append
            stack.append(c)
        elif c==')':

            if not stack:
                return False
            else:#닫힌 괄호인데 여는 괄호가 들어있다-> 맞는 쌍이 남아있다는 뜻 
                stack.pop()

    if stack:
        return False
    else:
        return True

print(solution("((())())"))
#solution("(())()")