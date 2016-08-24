n = 5
r,c = 2,3
grid = [['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','m','-'],
        ['-','-','-','-','-'],
        ['-','-','p','-','-']]

def nextMove(n,r,c,grid):
    [(px, py)] = [(i,j) for i in range(0,n) for j in range(0,n) if grid[i][j] == 'p']

    ## p and m in the same row
    if px == r :
        ## p and m are in different columns
        if py < c :
            return "LEFT"
        elif py > c :
            return "RIGHT"
        else :
            return ""
        #on this location p and m would be on the same location
    elif px < r :
        return "UP"
    elif px > r :
        return "DOWN"

print(nextMove(n,r,c,grid))
