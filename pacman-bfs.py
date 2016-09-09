'''
Input
11 9
2 15
13 20
%%%%%%%%%%%%%%%%%%%%
%----%--------%----%
%-%%-%-%%--%%-%.%%-%
%-%-----%--%-----%-%
%-%-%%-%%--%%-%%-%-%
%-----------%-%----%
%-%----%%%%%%-%--%-%
%-%----%----%-%--%-%
%-%----%-%%%%-%--%-%
%-%-----------%--%-%
%-%%-%-%%%%%%-%-%%-%
%----%---P----%----%
%%%%%%%%%%%%%%%%%%%%
Output
90
11 9
11 8
11 10
11 7
11 11
11 6
11 12
10 6
11 13
9 6
10 13
8 6
9 5
9 7
9 13
7 6
8 5
9 4
9 8
8 13
9 12
6 6
7 5
8 4
9 3
10 4
8 8
9 9
7 13
9 11
5 6
6 5
7 4
8 3
11 4
7 8
9 10
6 13
4 6
5 5
5 7
6 4
7 3
11 3
7 9
5 13
3 6
5 4
5 8
6 3
11 2
7 10
4 13
2 6
3 5
3 7
5 3
5 9
11 1
7 11
3 13
1 6
3 4
4 3
5 2
4 9
5 10
10 1
2 13
3 12
3 14
1 7
2 4
3 3
5 1
3 9
4 10
5 11
9 1
1 13
3 15
1 8
1 4
4 1
6 1
2 9
3 10
8 1
1 12
2 15
15
11 9
11 10
11 11
11 12
11 13
10 13
9 13
8 13
7 13
6 13
5 13
4 13
3 13
3 14
3 15
2 15
'''

#up, left, right, down
directions = [(-1,0),(0,-1),(0,1),(1,0)]
class Queue :
    def __init__(self):
        self.list = []
    
    def push(self, item):
        self.list.append(item)
        
    def pop(self):
        return self.list.pop(0)
    
    def isEmpty(self):
        return len(self.list) == 0
    
def getSuccessors(node, board):
    children = []
    x, y = node
    for dx,dy in directions:
        nextx, nexty = int(x + dx), int(y + dy)
        if not board[nextx][nexty] == '%':
            children.append((nextx,nexty))
    return children
    
def dfs_search(pacman, food, board):
    fringe = Queue()
    
    fringe.push((pacman, []))
    visited = []
    explored = []
    
    while not fringe.isEmpty():
        current_node, path = fringe.pop()
        explored.append(current_node)
        
        if current_node == food:
            return [visited + [current_node], path + [current_node]]
        
        if current_node not in visited:
            visited.append(current_node)
            
            x, y = current_node
            for node in getSuccessors(current_node, board):
                if node not in explored:
                    new_path = path + [current_node]
                    fringe.push((node,new_path))

if __name__ == '__main__':
    pacman = tuple(map(int, input().split()))
    food = tuple(map(int, input().split()))
    size = tuple(map(int, input().split()))
    # print(pacman,food,size)
    board = []
    for r in range(size[0]):
        board.append(list(input()))
    #print(board)
    explored, path = dfs_search(pacman,food,board)
    print(len(explored))
    for x, y in explored:
        print(x, y)
    print(len(path) - 1)
    for x, y in path:
        print(x, y)
