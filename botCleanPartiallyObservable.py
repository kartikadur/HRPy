#!/usr/bin/python3
import os
import pickle
from collections import OrderedDict

# --- test data ---
demo_board =[ [['b','d','o','o','o'],
                 ['-','d','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o']],
                [['-','d','-','o','o'],
                 ['-','d','-','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o']],
                [['-','b','-','o','o'],
                 ['-','d','-','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o']],
                [['-','-','-','o','o'],
                 ['-','d','-','o','o'],
                 ['-','-','-','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o']],
                [['-','-','-','o','o'],
                 ['-','b','-','o','o'],
                 ['-','-','-','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o']],
                [['o','-','-','-','o'],
                 ['o','-','b','-','o'],
                 ['o','-','-','d','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o']],
                [['o','o','o','o','o'],
                 ['o','-','-','-','o'],
                 ['o','-','b','d','o'],
                 ['o','-','-','d','o'],
                 ['o','o','o','o','o']],
                [['o','o','o','o','o'],
                 ['o','o','-','-','-'],
                 ['o','o','-','d','-'],
                 ['o','o','-','d','-'],
                 ['o','o','o','o','o']],
                [['o','o','o','o','o'],
                 ['o','o','-','-','-'],
                 ['o','o','-','b','-'],
                 ['o','o','-','d','-'],
                 ['o','o','o','o','o']],
                [['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','-','-','-'],
                 ['o','o','-','d','-'],
                 ['o','o','d','-','d']],
                [['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','-','-','-'],
                 ['o','o','-','b','-'],
                 ['o','o','d','-','d']],
                [['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','-','-','-'],
                 ['o','o','d','b','d']],
                [['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','-','-','-','o'],
                 ['o','-','d','-','o']],
                [['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','-','-','-','o'],
                 ['o','-','b','-','o']],
                [['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','-','-','-'],
                 ['o','o','-','b','d']],
                [['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','o','o'],
                 ['o','o','o','-','-'],
                 ['o','o','o','-','d']]]

robot_x = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4]
robot_y = [0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 2, 2, 3, 4]

# --- test data ---


def update_board(board) :
    if os.path.isfile("board") :
        old_board = pickle.load(open("board", "rb"))
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if board[i][j] == 'o' :
                    board[i][j] = old_board[i][j]
    pickle.dump(board, open("board", "wb"))

def next_move(posx, posy, board) :

    dirty_cells = {}
    blank_cells = {}
    cmd = ""

    update_board(board)
    
    for x in range(len(board)) :
        for y in range(len(board[0])) :
            if board[x][y] == 'd' :
                m_dist = abs(posx - x) + abs(posy - y)
                if m_dist in dirty_cells :
                    dirty_cells[m_dist].append((x,y))
                else :
                    dirty_cells[m_dist] = [(x,y)]
            if board[x][y] == 'o' :
                m_dist = abs(posx - x) + abs(posy - y)
                if m_dist in dirty_cells :
                    blank_cells[m_dist].append((x,y))
                else :
                    blank_cells[m_dist] = [(x,y)]

    
    #nothing to clean or explore
    if len(dirty_cells) == 0 and len(blank_cells) == 0 : return

    #dirty cells within visible range
    if len(dirty_cells) > 0 :
        dirty_cells = OrderedDict(sorted(dirty_cells.items(), key=lambda t: t[0]))
        #print(dirty_cells)
        (dx, dy) = next(iter(dirty_cells.items()))[1][0]
        #print(dirty_cells)

        
        if dx == posx and dy == posy :
            cmd = "CLEAN"
        if dy < posy :
            cmd = "LEFT"
        if dy > posy :
            cmd = "RIGHT"
        if dx < posx :
            cmd = "UP"
        if dx > posx :
            cmd = "DOWN"
            

    else :
        blank_cells = OrderedDict(sorted(blank_cells.items(), key=lambda t: t[0]))
        (bx, by) = next(iter(blank_cells.items()))[1][0]

        if bx < posx :
            cmd = "LEFT"
        elif bx > posx :
            cmd = "RIGHT"
        elif by < posy :
            cmd = "UP"
        else :
            cmd = "DOWM"

    print(cmd)

for i in range(len(demo_board)) :
    next_move(robot_x[i], robot_y[i], demo_board[i])
