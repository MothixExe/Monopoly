'''
Classe Board représentant le plateau de jeu.
'''

from Tile import Tile
from Property import Property
from ActionCase import Taxe, Jail, Gare, Compagnie
from Tirage import Tirage

class Board:
    '''
        Classe Board:
        - tiles: list, la liste des cases du plateau
    '''
    def __init__(self):
        self.tiles = [
            Tile("Départ", "start"),
            Property("Boulevard de Belleville", 60, [2, 10, 30, 90, 160, 250], 50, 50, "marron"),
            Tirage("Caisse de Communauté"),
            Property("Rue Lecourbe", 60, [4, 20, 60, 180, 320, 450], 50, 50, "marron"),
            Taxe("Impôts sur le revenu", 200),
            Gare("Gare Montparnasse", 200, 25, col="gare"),
            Property("Rue de Vaugirard", 100, [6, 30, 90, 270, 400, 550], 50, 50, "bleu clair"),
            Tirage("Chance"),
            Property("Rue de Courcelles", 100, [6, 30, 90, 270, 400, 550], 50, 50, "bleu clair"),
            Property("Avenue de la République", 120, [8, 40, 100, 300, 450, 600], 50, 50, "bleu clair"),
            Tile("Simple Visite / En prison", "jail"), # Case 10
            Property("Boulevard de la Villette", 140, [10, 50, 150, 450, 625, 750], 100, 100, "rose"),
            Compagnie("Compagnie de distribution d'électricité", 150, 0, col="compagnie"),
            Property("Avenue de Neuilly", 140, [10, 50, 150, 450, 625, 750], 100, 100, "rose"),
            Property("Rue de Paradis", 160, [12, 60, 180, 500, 700, 900], 100, 100, "rose"),
            Gare("Gare de Lyon", 200, 25, col="gare"),
            Property("Avenue Mozart", 180, [14, 70, 200, 550, 750, 950], 100, 100, "orange"),
            Tirage("Caisse de Communauté"),
            Property("Boulevard Saint-Michel", 180, [14, 70, 200, 550, 750, 950], 100, 100, "orange"),
            Property("Place Pigalle", 200, [16, 80, 220, 600, 800, 1000], 100, 100, "orange"),
            Tile("Parc Gratuit", "parking"),
            Property("Avenue Matignon", 220, [18, 90, 250, 700, 875, 1050], 150, 150, "rouge"),
            Tirage("Chance"),
            Property("Boulevard Malesherbes", 220, [18, 90, 250, 700, 875, 1050], 150, 150, "rouge"),
            Property("Avenue Henri-Martin", 240, [20, 100, 300, 750, 925, 1100], 150, 150, "rouge"),
            Gare("Gare du Nord", 200, 25, col="gare"),
            Property("Faubourg Saint-Honoré", 260, [22, 110, 330, 800, 975, 1150], 150, 150, "jaune"),
            Property("Place de la Bourse", 260, [22, 110, 330, 800, 975, 1150], 150, 150, "jaune"),
            Compagnie("Compagnie de distribution d'électricité", 150, 0, col="compagnie"),
            Property("Rue La Fayette", 280, [24, 120, 360, 850, 1025, 1200], 150, 150, "jaune"),
            Jail("Allez en prison", "go_to_jail"),
            Property("Avenue de Breteuil", 300, [26, 130, 390, 900, 1100, 1275], 200, 200, "vert"),
            Property("Avenue Foch", 300, [26, 130, 390, 900, 1100, 1275], 200, 200, "vert"),
            Tirage("Caisse de Communauté"),
            Property("Boulevard des Capucines", 320, [28, 150, 450, 1000, 1200, 1400], 200, 200, "vert"),
            Gare("Gare Saint-Lazare", 200, 25, col="gare"),
            Tirage("Chance"),
            Property("Avenue des Champs-Élysées", 350, [35, 175, 500, 1100, 1300, 1500], 200, 200, "bleu"),
            Taxe("Taxe de luxe", 100),
            Property("Rue de la Paix", 400, [50, 200, 600, 1400, 1700, 2000], 200, 200, "bleu"),
        ]
        self.creer_soeurs()

    def creer_soeurs(self):
        '''
            Méthode creer_soeurs:
            Crée les groupes de propriétés soeurs.
        '''
        for i, tile in enumerate(self.tiles):
            if isinstance(tile, Property):
                for j in range(i + 1, len(self.tiles)):
                    if isinstance(self.tiles[j], Property) and tile.col == self.tiles[j].col:
                        tile.add_sister(self.tiles[j])

    def display(self, players):
        '''
            Méthode display:
            - players: list, la liste des joueurs
            Affiche le plateau de jeu.
        '''
        for idx, tile in enumerate(self.tiles):
            players_on_tile = [p.name for p in players if p.position == idx]
            player_display = " | ".join(players_on_tile)
            print(f"{idx}: {tile.name} ({tile.tile_type}) {'-> ' + player_display if player_display else ''}")
