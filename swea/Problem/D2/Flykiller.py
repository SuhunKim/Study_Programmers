# 파리퇴치 T는 5~15 각 셀 값 0~30

T= int (input())

for i in range(T):
    n,m = map(int,input().split())    # n : 배열 크기 m : 파리채
    # m = int (input())   # 파리채
    if(m<2 or m>n):
        break

    # square = [[0 for _ in range(n)] for _ in range(n)]
    square = []

    for _ in range(n):
        a = list(map(int, input().split()))
        square.append(a)    
    # for j in range(n):
        # for k in range(n):
            # square[j][k] = int(input().split())    #map(int,input().split())

    list_sum = []
    for row in range(0,n-1,1):
        if(row<n-(m-1)):

            for col in range(0,n-1,1):
                if(col<n-(m-1)):
                    sum = 0
                    for r in range(m):
                        for c in range(m):
                            #4중 포문 사용안하고 하는 방법 찾기
                            sum+=square[row+r][col+c]
                        
                    # list_sum.append(square[row+r][col+c])
                    list_sum.append(sum)
    

    print('#'+str(i+1)+' '+str(max(list_sum)))


