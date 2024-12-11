'''
    Ce fichier contient la classe Player qui représente un joueur dans le jeu.
    Un joueur est caractérisé par son nom, sa position sur le plateau de jeu,
    son argent, les propriétés qu'il possède, s'il est en prison ou non,
    le nombre de propriétés qu'il possède.
'''

class Player:
    '''
        Classe Player:
        - name: str, le nom du joueur
        - position: int, la position du joueur sur le plateau
        - money: int, l'argent du joueur
        - properties: list, la liste des propriétés que le joueur possède
        - prisonier: list, [bool, int], si le joueur est en prison ou non
    '''

    def __init__(self, name):
        self.name = name
        self.position = 1
        self.money = 1500
        self.properties = []
        self.prisonier = [False, 0]

    def move(self, steps, board_size):
        '''
            Méthode move:
            - steps: int, le nombre de cases que le joueur doit avancer
            - board_size: int, la taille du plateau
            Avance le joueur de steps cases sur le plateau de taille board_size.
        '''
        self.position = (self.position + steps) % board_size
        print(f"{self.name} avance de {steps} cases et se trouve sur la case {self.position}.")

    def upgrade_property(self, prop):
        '''
            Méthode upgrade_property:
            - prop: Property, la propriété à améliorer
            Améliore la propriété prop si le joueur possède cette propriété.    
        '''
        if prop in self.properties:
            prop.upgrade(self)
        else:
            print(f"{self.name} ne possède pas {prop.name}.")

    def get_current_tile(self, Game):
        '''
            Méthode get_current_tile:
            Retourne la case sur laquelle le joueur se trouve.
        '''
        return Game.board.tiles[self.position]

    def faillite(self):
        '''
            Méthode faillite:
            Met fin à la partie pour le joueur.
        '''
        print(f"{self.name} est en faillite !")
        print("Toutes ses propriétés sont maintenant disponibles")
        self.properties = []
