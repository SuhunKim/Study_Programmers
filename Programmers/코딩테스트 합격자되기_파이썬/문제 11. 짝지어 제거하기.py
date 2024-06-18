def solution(s):
    stack=[]
    for c in s:
        # stack[-1]은 stack의 top, 즉, 이 위치에는 최근에 추가한 데이터가 있습니다. 
        #다만 스택이 빈 경우도 고려해야 하므로 top 위치의 원소값부터 체크하지 말고 반드시 stack이 비었는지 체크해야 합니다.
        if stack and stack[-1]==c:
            stack.pop()
        else:
            stack.append(c)
        
    return int(not stack) #스택이 비어있으면 1 아니면 0