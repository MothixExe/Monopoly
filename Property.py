'''
Classe Property, héritant de Tile, représentant une propriété du plateau de jeu.
'''

from Tile import Tile

class Property(Tile):
    '''
        Classe Property:
        - cost: int, le coût d'achat de la propriété
        - list_rent: list, la liste des loyers de la propriété
        - house_count: int, le nombre de maisons sur la propriété
        - house_price: int, le prix d'une maison
        - hotel_price: int, le prix d'un hôtel
        - col: str, la couleur de la propriété
        - sister: list, la liste des propriétés de la même couleur
        - owner: Player, le propriétaire de la propriété
    '''
    def __init__(self, name, cost, list_rent=None, house_price=None, hotel_price=None, col=None):
        super().__init__(name, "property")
        self.cost = cost
        self.list_rent = list_rent
        self.house_count = 0 # La cinquième maison est un hôtel
        self.house_price = house_price
        self.hotel_price = hotel_price
        self.col = col
        self.sister = [] # Liste des propriétés de la même couleur
        self.owner = None

    def add_sister(self, sister):
        '''
            Méthode add_sister:
            - sister: Property, la propriété à ajouter à la liste des propriétés soeurs
            Ajoute une propriété à la liste des propriétés soeurs.
        '''
        self.sister.append(sister)

    def check_if_monopoly(self):
        '''
            Méthode check_if_monopoly:
            Retourne True si le joueur possède toutes les propriétés de la même couleur, False sinon.
        '''
        return all(s.owner == self.owner for s in self.sister)

    def get_upgrade_cost(self):
        '''
            Méthode get_upgrade_cost:
            Retourne le coût de l'amélioration de la propriété.
        '''
        return self.house_price if self.house_count < 4 else self.hotel_price

    def upgrade(self, player):
        '''
            Méthode upgrade:
            - player: Player, le joueur améliorant la propriété
            Améliore la propriété si le joueur possède toutes les propriétés de la même couleur.
        '''
        if self.house_count < 5 and self.check_if_monopoly():
            if player.money >= self.get_upgrade_cost():
                player.money -= self.get_upgrade_cost()
                self.house_count += 1
                print(f"{player.name} a amélioré {self.name}. Il reste {player.money}€.")
            else:
                print(f"{player.name} n'a pas assez d'argent pour améliorer {self.name}.")
        else:
            print(f"{self.name} ne peut pas être amélioré.")

    def action(self, player):
        '''
            Méthode action:
            - player: Player, le joueur arrivant sur la propriété
            Effectue l'action correspondant à l'arrivée du joueur sur la propriété.
        '''
        if self.owner is None:
            print(f"{player.name} arrive sur {self.name}, coût : {self.cost}€, loyer : {self.list_rent[self.house_count]}€.")
            print("1. Acheter")
            print("2. Ne rien faire")
            choix = input("Que voulez-vous faire ? (1/2) ")
            if choix == "1" and player.money >= self.cost:
                player.money -= self.cost
                player.properties.append(self)
                self.owner = player
                print(f"{player.name} a acheté {self.name}. Il reste {player.money}€.")
            elif choix == "1":
                print(f"{player.name} n'a pas assez d'argent pour acheter {self.name}.")
        elif self.owner == player:
            print(f"{player.name} arrive sur {self.name}.")
            if self.check_if_monopoly():
                print("Vous possédez toutes les propriétés de cette couleur.")
                print("1. Améliorer cette propriété")
                print("2. Ne rien faire")
                choix = input("Que voulez-vous faire ? (1/2) ")
                if choix == "1":
                    player.upgrade_property(self)
        else:
            print(f"{player.name} arrive sur {self.name}, appartenant à {self.owner.name}.")
            loyer = self.list_rent[self.house_count]
            if player.money >= loyer:
                player.money -= loyer
                self.owner.money += loyer
                print(f"{player.name} paie {loyer}€ de loyer à {self.owner.name}. Solde restant : {player.money}€.")
            else:
                print(f"{player.name} n'a pas assez d'argent pour payer le loyer !")
                # Gestion de la faillite pourrait être ajoutée ici
