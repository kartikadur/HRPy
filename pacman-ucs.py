'''
Input
35 35
35 1
37 37
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%-------%-%-%-----------%---%-----%-%
%-%%%%%%%-%-%%%-%-%%%-%%%-%%%%%%%-%-%
%-------%-------%-%-----%-----%-%---%
%%%%%-%%%%%-%%%-%-%-%-%%%-%%%%%-%-%%%
%---%-%-%-%---%-%-%-%---%-%---%-%---%
%-%%%-%-%-%-%%%-%%%%%-%%%-%-%%%-%%%-%
%-------%-----%---%---%-----%-%-%---%
%%%-%%%%%%%%%-%%%%%%%-%%%-%%%-%-%-%-%
%-------------%-------%-%---%-----%-%
%-%-%%%%%-%-%%%-%-%-%%%-%-%%%-%%%-%-%
%-%-%-----%-%-%-%-%-----%---%-%-%-%-%
%-%-%-%%%%%%%-%-%%%%%%%%%-%%%-%-%%%-%
%-%-%-%-----%---%-----%-----%---%---%
%%%-%%%-%-%%%%%-%%%%%-%%%-%%%-%%%%%-%
%-----%-%-%-----%-%-----%-%---%-%-%-%
%-%-%-%-%-%%%-%%%-%%%-%%%-%-%-%-%-%-%
%-%-%-%-%-----------------%-%-%-----%
%%%-%%%%%%%-%-%-%%%%%-%%%-%-%%%-%%%%%
%-------%-%-%-%-----%---%-----%-%---%
%%%%%-%-%-%%%%%%%%%-%%%%%%%%%%%-%-%%%
%---%-%-----------%-%-----%---%-%---%
%-%%%-%%%%%-%%%%%%%%%-%%%%%-%-%-%%%-%
%-%---%------%--------%-----%-------%
%-%-%-%%%%%-%%%-%-%-%-%-%%%%%%%%%%%%%
%-%-%---%-----%-%-%-%-------%---%-%-%
%-%-%%%-%%%-%-%-%-%%%%%%%%%-%%%-%-%-%
%-%---%-%---%-%-%---%-%---%-%-%-----%
%-%%%-%%%-%%%%%-%%%-%-%-%%%%%-%-%%%%%
%-------%---%-----%-%-----%---%-%---%
%%%-%-%%%%%-%%%%%-%%%-%%%-%-%%%-%-%%%
%-%-%-%-%-%-%-%-----%-%---%-%---%-%-%
%-%-%%%-%-%-%-%-%%%%%%%%%-%-%-%-%-%-%
%---%---%---%-----------------%-----%
%-%-%-%-%%%-%%%-%%%%%%%-%%%-%%%-%%%-%
%.%-%-%-------%---%-------%---%-%--P%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Output
210
35 35
34 35
33 35
33 34
33 33
33 32
33 31
32 31
31 31
31 30
31 29
32 29
33 29
33 28
33 27
33 26
33 25
33 24
33 23
33 22
33 21
33 20
33 19
33 18
33 17
33 16
33 15
32 15
31 15
31 16
31 17
30 17
29 17
29 16
29 15
28 15
27 15
26 15
25 15
24 15
23 15
23 16
23 17
23 18
23 19
23 20
23 21
24 21
25 21
25 22
25 23
24 23
23 23
23 24
23 25
23 26
23 27
22 27
21 27
21 28
21 29
22 29
23 29
23 30
23 31
22 31
21 31
20 31
19 31
18 31
17 31
17 32
17 33
17 34
17 35
16 35
15 35
14 35
13 35
12 35
11 35
10 35
9 35
8 35
7 35
7 34
7 33
8 33
9 33
9 32
9 31
9 30
9 29
10 29
11 29
12 29
13 29
14 29
15 29
15 28
15 27
16 27
17 27
18 27
19 27
19 26
19 25
18 25
17 25
17 24
17 23
17 22
17 21
17 20
17 19
17 18
17 17
17 16
17 15
17 14
17 13
16 13
15 13
15 14
15 15
14 15
13 15
12 15
11 15
10 15
9 15
9 16
9 17
9 18
9 19
9 20
9 21
8 21
7 21
6 21
5 21
4 21
3 21
2 21
1 21
1 20
1 19
1 18
1 17
1 16
1 15
2 15
3 15
3 14
3 13
3 12
3 11
4 11
5 11
6 11
7 11
7 12
7 13
8 13
9 13
9 12
9 11
9 10
9 9
9 8
9 7
9 6
9 5
9 4
9 3
10 3
11 3
12 3
13 3
14 3
15 3
16 3
17 3
18 3
19 3
19 4
19 5
20 5
21 5
22 5
23 5
23 4
23 3
24 3
25 3
26 3
27 3
27 4
27 5
28 5
29 5
29 4
29 3
30 3
31 3
32 3
33 3
33 2
33 1
34 1
35 1
'''
#up, left, right, down
from heapq import heappush, heappop

directions = [(-1,0),(0,-1),(0,1),(1,0)]

class PriorityQueue :
    def __init__(self, priorityFunc):
        self.priorityFunc = priorityFunc
        self.heap = []
        self.count = 0
    
    def push(self, item):
        entry = (self.priorityFunc, self.count, item)
        heappush(self.heap, entry)
        self.count += 1
        
    def pop(self):
        (_, _, item) = heappop(self.heap)
        return item
    
    def isEmpty(self):
        return len(self.heap) == 0

def costOfActions(actions):
    if actions == None: return 999999
    cost = 0
    for action in actions:
        x, y = action
        if board[x][y] == '%': return 999999
        cost += 1
    return cost
        
def getSuccessors(node, board):
    children = []
    x, y = node
    for dx,dy in directions:
        nextx, nexty = int(x + dx), int(y + dy)
        if not board[nextx][nexty] == '%':
            children.append((nextx,nexty))
    return children
    
def dfs_search(pacman, food, board):
    priorityFunc = lambda actions: costOfActions([x for x in actions[1]])
    fringe = PriorityQueue(priorityFunc)
    
    fringe.push((pacman, []))
    visited = []
    explored = []
    
    while not fringe.isEmpty():
        current_node, path = fringe.pop()
        explored.append(current_node)
        
        if current_node == food:
            return path + [current_node]
        
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
    path = dfs_search(pacman,food,board)
    print(len(path) - 1)
    for x, y in path:
        print(x, y)
