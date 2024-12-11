'''
Classe Tile, représentant une case du plateau de jeu.
'''

class Tile:
    '''
        Classe Tile:
        - name: str, le nom de la case
        - tile_type: str, le type de la case
    '''
    def __init__(self, name, tile_type):
        self.name = name
        self.tile_type = tile_type
        self.col = None

    def action(self, player):
        '''
            Méthode action:
            - player: Player, le joueur arrivant sur la case
            Effectue l'action associée à la case.
        '''
        print(f"{player.name} arrive sur {self.name}.")
