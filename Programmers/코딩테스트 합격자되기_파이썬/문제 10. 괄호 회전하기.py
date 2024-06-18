

def solution(s):
    cnt = 0

    for i in len(s):
        stack = []

        str = s

        c=""

        if c == "(" or c == "[" or c == "{":  # ➋ 열린 괄호는 푸시
            stack.append(c)
        else:
            if not stack:
                break

            if c == ")" and stack[-1] == "(":
                stack.pop( ) 
            elif c == "]" and stack[-1] == "[":
                stack.pop( ) 
            elif c == "}" and stack[-1] == "{":
                stack.pop( ) 
            else:
             break