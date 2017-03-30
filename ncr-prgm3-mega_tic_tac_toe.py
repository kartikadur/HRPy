##import numpy as np
## input
##5
##3 3 3
##XOX
##XOX
##XXX
##3 3 3
##X-X
##O-O
##X-X
##3 3 3
##O-X
##XOO
##XOO
##3 3 3
##O-X
##O-X
##O-X
##4 5 3
##-----
##-X---
##--XOO
##--O-X
##5 4 3
##----
##-X--
##--XO
##--O-
##-O--
## output
##LOSE
##NONE
##WIN
##NONE
##NONE

def ret_diags(num):
    return [(i,i) for i in range(num)]

def adjust_diag(diag, offset):
    return [(r-offset, c) for (r,c) in diag]

def in_matrix(mat_b, d_co):
    return 0<=d_co[0]<mat_b[0] and 0<=d_co[1]<mat_b[1]

def diagonal_coordinates(r, c, k):
    diags = []
    for offset in reversed(range(-c + 1, r)):
        diagonal = [d for d in adjust_diag(ret_diags(r + c - 1), offset) if in_matrix([r, c], d)]
##        print(diagonal)
        if len(diagonal) >= k:
            diags.append(diagonal)
    return diags
                           
 
## param -- board, rows, columns, wins
def predict_win(b, r, c, w):
    xs = ['X' for _ in range(k)]
    os = ['O' for _ in range(k)]
    win_x = []
    win_o = []

    for i in range(r):
        for j in range(c - k + 1):
            print(b[i][j:j+k], i, j, k, j+k)
            win_x.append(b[i][j:j+k] == xs)
            win_o.append(b[i][j:j+k] == os)

##    get diags

    diags = diagonal_coordinates(r, c, w)
    b_diags = []
    b_diags.extend([[b[x][y] for x,y in row] for row in diags])
    for i in range(n): b[i] = list(reversed(b[i]))
    b_diags.extend([[b[x][y] for x,y in row] for row in diags])
    

##    diags.append( [ row[i - 2] for i, row in enumerate(b) ])
    
##    diags.append( [row[i+offset] for i, row in enumerate(b) if 0 <= i + offset < len(row)])
##    diags.append( [ row[-i-1] for i, row in enumerate(b)])

##    diags = [b[::-1,:].diagonal(i) for i in range(r + 1,c)]
##    diags.extend(b.diagonal(i) for i in range(r - 1, -c, -1))
##    b_diags = [n.tolist() for n in diags if len(n) >= k]
    
    for i in range(len(b_diags)):
        for j in range(len(b_diags[i]) - k + 1):
            win_x.append(b_diags[i][j:j+k] == xs)
            win_o.append(b_diags[i][j:j+k] == os)

##    transpose
    b = list(map(list, zip(*b)))
    for i in range(c):
        for j in range(r - k + 1):
            win_x.append(b[i][j:j+k] == xs)
            win_o.append(b[i][j:j+k] == os)

    if True in win_o and True in win_x:
        return 'NONE'
    if True in win_o and True not in win_x:
        return 'WIN'
    if True not in win_o and True in win_x:
        return 'LOSE'
    if True not in win_o and True not in win_x:
        return 'NONE'

if __name__ == '__main__':
    g = int(input().strip())
    for i in range(g):
        n, m, k = list(map(int, input().strip().split()))
        board = []
        for j in range(n):
            row = input().strip()
            board.append([a for a in row])

##        print(board)
        print(predict_win(board, n, m, k))
