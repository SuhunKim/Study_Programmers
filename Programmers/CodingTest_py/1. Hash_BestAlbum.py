def solution(genres, plays):
    answer=0
    list_each = []
    dict_1={}

    for i in range(len(genres)):
        list_each.append([i,genres[i],plays[i]])
        if genres[i] in dict_1:
            dict_1[genres[i]]+=plays[i]
        else :
            dict_1[genres[i]]=plays[i]

    #장르 순 출력
    more=0
    list_order_genre=[]
    for key,value in dict_1.items():
        if  more < value:
            more=i
            list_order_genre.insert(0,key)


    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))