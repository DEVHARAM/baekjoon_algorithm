def bfs():
    visit = [False] * (F + 1)
    visit[S] = True
    Q = []
    Q.append(S)

    level = 0
    while (len(Q) != 0):
        for _ in range(len(Q)):
            floor = Q.pop(0)
            if (floor == G):
                print(level)
                return
            tempNext = floor + U
            if (tempNext <= F and not visit[tempNext]):
                Q.append(tempNext)
                visit[tempNext] = True
            tempNext = floor - D
            if (tempNext > 0 and not visit[tempNext]):
                Q.append(tempNext)
                visit[tempNext] = True
            print(Q)
        level += 1
    print('use the stairs')
    return    
F,S,G,U,D=map(int,input().split())
bfs()