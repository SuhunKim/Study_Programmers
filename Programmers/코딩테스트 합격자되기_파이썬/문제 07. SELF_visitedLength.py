def update_location(x, y, dir) : # ➋ 명령어를 통해 다음 좌표 결정
    if dir=='U':
        y+=1
    elif dir=='D':
        y-=1
    elif dir=='L':
        x-=1
    elif dir =='R':
        x+=1
    return x,y

def is_valid_move(nx, ny) : # ➊ 좌표평면을 벗어나는지 체크하는 함수
    return 0<=nx<11 and 0<=ny<11

def solution(dirs):
    x,y = 5,5
    listdir=list(dirs)
    answer = set()
    
    for dir in dirs:
        nx,ny = update_location(x,y,dir)
        if not is_valid_move(nx,ny):    #벗어난 좌표로 이동하는 명령어는 무시하고 넘어감
            continue
        answer.add((x, y, nx, ny))  #양방향 경로 Add
        answer.add((nx, ny, x, y))
        x,y = nx,ny             # 이동

    return round( len(answer)/2)

print(solution("ULURRDLLU"))
