import random
from player import Player


class Game(): 

    COLORS = ['red', 'blue', 'yellow', 'green']

    def __init__(self, player_names, colors=COLORS): 
        if isinstance(player_names, list): 
            if all(isinstance(s, str) for s in player_names):
                if len(player_names) in (2, 4): 
                    self.player_names = player_names
                    self.colors = colors
                    self.players = None 
                else: 
                    raise ValueError('Please enter only 2 or 4 player names')    
            else: 
                raise TypeError('Please enter only strings for player name')
        else: 
            raise TypeError('Please enter a list of strings for player_names')


    @property
    def players(self): 
        return self._players 


    @players.setter
    def players(self, players): 
        ps = []
        player_nums = [x for x in range(len(self.player_names))]
        random.shuffle(self.colors)
        random.shuffle(player_nums)
        for name in self.player_names: 
            player = Player(name, self.colors.pop(), player_nums.pop())
            ps.append(player)
        self._players = ps    
            

if __name__ == '__main__': 
    g = Game(['Maxwell', 'Franklin', 'Desiree', 'Jill'])
    print(g.players)
