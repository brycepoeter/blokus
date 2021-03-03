


class Tile(): 

    def __init__(self, occupied_by=None): 
        self.occupied_by = occupied_by
        self.neighbors = set()


    def __repr__(self): 
        return f'Tile Occupied by {self.occupied_by}'    
        

