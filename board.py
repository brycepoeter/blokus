import numpy as np
from tile import Tile

class Board(): 

    def __init__(self, dimension): 
        self.dimension = dimension
        self.info = None


    def __repr__(self): 
        return f'{self.info}'    


    @property
    def info(self): 
        return self._info


    @info.setter
    def info(self, info): 
        board = np.full((self.dimension, self.dimension), Tile())
        self._info = board


if __name__ == '__main__': 
    b = Board(8)
    print(b)

                

