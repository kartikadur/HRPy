from collections import OrderedDict
import math
posr_1, posc_1 = 0, 0
board = [['b','-','-','-','d'],
         ['-','d','-','-','d'],
         ['-','-','d','d','-'],
         ['-','-','d','-','-'],
         ['-','-','-','-','d']]

board_1 = [['b','d','d','d','d'],
         ['d','-','-','-','-'],
         ['d','-','-','-','-'],
         ['d','-','-','-','-'],
         ['d','-','-','-','d']]

def next_move(posr, posc, board):

    dirty_cells = {}

    for i in range(0, len(board)) :
        for j in range(0, len(board[0])) :
            if board[i][j] == "d" :
                key = abs(i - posr) + abs(j - posc)
                if key in dirty_cells :
                    dirty_cells[key].append((i,j))
                else :
                    dirty_cells[key] = [(i,j)]

    # no dirty cells
    if len(dirty_cells) == 0 : return (-1, -1)

    # order dirty cells by proximity
    dirty_cells = OrderedDict(sorted(dirty_cells.items(), key=lambda t: t[0]))

    #gets a dirty cell closest to the bot
    (dx, dy) = next(iter(dirty_cells.items()))[1][0]

    # dirty cell and bot in same row
    if(posr == dx) :
        # dirty cell and bot in same col : thus in same cell
        if(posc == dy) :
            board[dx][dy] = '-'
            print("CLEAN")
        # dirty cell is left of bot in same row
        elif (posc < dy) :
            posc += 1
            print("RIGHT")
        # dirty cell is right of bot in same row
        else :
            posc -= 1
            print("LEFT")
    # dirty cell is above bot
    elif( posr < dx ) :
        posr += 1
        print("DOWN")
    #dirty cell is below bot
    else :
        posr -= 1
        print("UP")
    return (posr, posc)

(posr_1, posc_1) = next_move(posr_1, posc_1, board_1)
while posr_1 != -1 and posc_1 != -1:
    (posr_1, posc_1) = next_move(posr_1, posc_1, board_1)
