board = [['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%'],
         ['%', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '%', '-', '-', '-', '%'],
         ['%', '-', '%', '%', '-', '%', '%', '-', '%', '%', '-', '%', '%', '-', '%', '%', '-', '%', '-', '%'],
         ['%', '-', '-', '-', '-', '-', '-', '-', '-', 'P', '-', '-', '-', '-', '-', '-', '-', '%', '-', '%'],
         ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '-', '%'],
         ['%', '.', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '%'],
         ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%']]

pacman = (3,9)
food = (5,1)
size = (7,20)
##game_2 = [25 13
##3 1
##27 28
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##%------------%%------------%
##%-%%%%-%%%%%-%%-%%%%%-%%%%-%
##%.%%%%-%%%%%-%%-%%%%%-%%%%-%
##%-%%%%-%%%%%-%%-%%%%%-%%%%-%
##%--------------------------%
##%-%%%%-%%-%%%%%%%%-%%-%%%%-%
##%-%%%%-%%-%%%%%%%%-%%-%%%%-%
##%------%%----%%----%%------%
##%%%%%%-%%%%%-%%-%%%%%-%%%%%%
##%%%%%%-%%%%%-%%-%%%%%-%%%%%%
##%%%%%%-%------------%-%%%%%%
##%%%%%%-%-%%%%--%%%%-%-%%%%%%
##%--------%--------%--------%
##%%%%%%-%-%%%%%%%%%%-%-%%%%%%
##%%%%%%-%------------%-%%%%%%
##%%%%%%-%-%%%%%%%%%%-%-%%%%%%
##%------------%%------------%
##%-%%%%-%%%%%-%%-%%%%%-%%%%-%
##%-%%%%-%%%%%-%%-%%%%%-%%%%-%
##%---%%----------------%%---%
##%%%-%%-%%-%%%%%%%%-%%-%%-%%%
##%%%-%%-%%-%%%%%%%%-%%-%%-%%%
##%------%%----%%----%%------%
##%-%%%%%%%%%%-%%-%%%%%%%%%%-%
##%------------P-------------%
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
##game_3 = [11 9
##2 15
##13 20
##%%%%%%%%%%%%%%%%%%%%
##%----%--------%----%
##%-%%-%-%%--%%-%.%%-%
##%-%-----%--%-----%-%
##%-%-%%-%%--%%-%%-%-%
##%-----------%-%----%
##%-%----%%%%%%-%--%-%
##%-%----%----%-%--%-%
##%-%----%-%%%%-%--%-%
##%-%-----------%--%-%
##%-%%-%-%%%%%%-%-%%-%
##%----%---P----%----%
##%%%%%%%%%%%%%%%%%%%%]

def pacman_dfs(pacman, food, maze) :
    
    stack = [(pacman, [])]
    visited = []
    
    while len(stack) != 0 :
        n, path = stack.pop()
        visited.append(n)
        
        if n == food :
            # print no. of nodes touched
            print(len(visited))
            # print nodes touched
            for node in visited :
                print("{0} {1}".format(node[0],node[1]))
            # print no. of nodes in path
            print(len(path))
            # print nodes in path
            #but for now
            for node in path :
                print("{0} {1}".format(node[0],node[1]))
            print(n[0],n[1])
        

        #getchildren for unvisited nodes
        #up r-1,c
        if maze[n[0] - 1][n[1]] != '%' and (n[0] - 1, n[1]) not in visited:
            stack.append(((n[0] - 1,n[1]), path + [n]))
        #left r,c-1
        if maze[n[0]][n[1] - 1] != '%' and (n[0], n[1] - 1) not in visited:
            stack.append(((n[0],n[1] - 1), path + [n]))
        #right r,c+1
        if maze[n[0]][n[1] + 1] != '%' and (n[0], n[1] + 1) not in visited:
            stack.append(((n[0],n[1] + 1), path + [n]))
        #down r+1,c
        if maze[n[0] + 1][n[1]] != '%' and (n[0] + 1, n[1]) not in visited:
            stack.append(((n[0] + 1,n[1]), path + [n]))

##if __name__ == "__main__" :
##    pacman = tuple(map(int, input().strip().split()))
##    food = tuple(map(int, input().strip().split()))
##    dim = tuple(map(int, input().strip().split()))
##    board = []
##    for i in range(dim[0]) :
##        board.append(list(input()))
pacman_dfs(pacman, food, board)

