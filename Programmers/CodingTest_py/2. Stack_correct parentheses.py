def solution(s):
    answer = True
    
    ST = []
    for i in range(len(s)):
        a = s[i]
        
        if a == '(':
            ST.append(a)
        else:
            if len(ST)==0:
                return False
            else:
                ST.pop()
    
    if len(ST) != 0:
        return False
    
    return True


print(solution("()()"))