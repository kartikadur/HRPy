#!/bin/python

class Tile:

    def __init__(self, color, posx = -1, posy = -1,
                 up = None, down = None,
                 right = None, left = None) :
        #tile color
        self.color = color

        self.position = (posx, posy)

        #neighbors
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def isSameColor(self, tile) :
        # return true if colors are equal
        return self.color == tile.color

    def isManhattanNeighbor(self, tile) :
        return abs(self.position[0] - tile.position[0]) + abs(self.position[1] - tile.position[1])


if __name__ == "__main__" :

    tile = Tile('R')
    print(tile)
