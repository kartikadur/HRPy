grid = [['-', '-', 'p'], ['-', 'm', '-'], ['-', '-', '-']]
n = 3

def displayPathtoPrincess(n,grid):
    # find princess
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "p" :
                py, px = i, j
            if grid[i][j] == "m" :
                my, mx = i, j

    while px != mx and py != my :
        # princess above bot
        if px < mx :
            mx -= 1
            print("UP")
        # princess below bot
        if px > mx :
            mx += 1
            print("DOWN")
        # princess to left of bot
        if py < my :
            my -= 1
            print("LEFT")
        # princess to right of bot
        if py > my :
            my += 1
            print("RIGHT")
   
    


displayPathtoPrincess(n,grid)
