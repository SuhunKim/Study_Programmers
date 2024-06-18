# 초 단위로 기록된 주식 가격이 담긴 배열 prices가 매개변수로 주어질 때, 
# 가격이 떨어지지 않은 기간은 몇 초인지를 반환

def solution(prices):
    stack=[]

    for i in prices:
        