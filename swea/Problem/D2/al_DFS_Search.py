TC = int(input())

visit = []
max_Edge=-1

myGraph = {
    "1": ["2", "3"],
    "2": ["1", "7","4"],
    "3": ["1","5", "6"],
    "4": ["2", "7"],
    "5": ["3", "7"],
    "6": [ "3","7"],
    "7": ["2","4","5","6"]
    }

# def my_dfs(graph, start_node):
#     visited = list() # 방문한 노드를 담을 배열
#     stack = list() # 정점과 인접한 방문 예정인 노드를 담을 배열

#     stack.append(start_node) # 처음에는 시작 노드 담아주고 시작하기.

#     while stack: # 더 이상 방문할 노드가 없을 때까지.
#         node = stack.pop() # 방문할 노드를 앞에서 부터 하나씩 꺼내기.

#         if node not in visited: # 방문한 노드가 아니라면
#             visited.append(node) # visited 배열에 추가
            
#             stack.extend(graph[node]) # 해당 노드의 자식 노드로 추가
#             # stack.extend(reversed(graph[node])) #오른쪽부터

#     print("dfs - ", visited)
#     return visited
    
#     # 함수 실행
# my_dfs(myGraph, 'G',)

def depthFirstSearch(start, depth):
    if(start==End):
        if max_Edge<0 or depth<max_Edge:
            max_Edge=depth
        return 
    visit[v]=1

    for v in range(1,Vs,1):
        if(map[v][i]==1 and visit[i]==0):
            depthFirstSearch(i,depth+1)
            visit[i]=0


    return 


for i in range(TC):
    Vs,Es,Start,End = map(int,input().split())  #정점, 간선, 시작점, 도착점
    
    lEdge = []

    for e in range(Es   ):
        a,b=map(int,input ().split())
        myGraph[a][b]=1
    max_Edge=1

    depthFirstSearch(Start,0)

    print("#"+str(i+1)+" "+str(max_Edge))
