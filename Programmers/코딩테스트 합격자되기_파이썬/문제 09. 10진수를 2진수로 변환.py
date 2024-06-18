#10진수를 입력받아 2진수로 변환해서 반환

#10진수 N을 진수 M으로 나눈 나머지를 저장, 2로 나눔
#몫이 0이 될 때까지 1을 수행
#저장한 수를 뒤부터 순서대로 가져와 붙이기

def solution(dec):
    stack = []

    while ( dec!=0):
        a=dec%2
        dec//=2

        stack.append(str(a))
        if(dec==0):
            break

    stack.reverse()
    binary= ''.join(stack)

    return str(binary)


print(solution(10))