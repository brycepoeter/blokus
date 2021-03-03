

class Player(): 

    def __init__(self, name, color, uid): 
        self.name = name
        self.color = color
        self.uid = uid


    def __repr__(self): 
        return f'{self.color.capitalize()} Player: {self.name}'    


