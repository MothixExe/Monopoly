'''
Classe pour les cases spéciales du plateau de jeu (propriétés, gares, compagnies, prison, taxes).
'''
from Property import Property
from Tile import Tile

class Compagnie(Property):
    '''
        Classe Compagnie, héritant de Property, représentant une compagnie de distribution d'électricité ou d'eau.
    '''
    def __init__(self, name, cost, rent, col):
        super().__init__(name, cost, rent, col=col)
        self.name = name
        self.cost = cost
        self.rent = rent
        self.col = col

    def action(self, player, dice):
        if self.owner is None:
            print(f"{player.name} arrive sur {self.name}, coût : {self.cost}€, loyer : {self.rent}€.")
            print("1. Acheter")
            print("2. Ne rien faire")
            choice = input("Que voulez-vous faire ? (1/2) ")
            if choice == "1" and player.money >= self.cost:
                player.money -= self.cost
                player.properties.append(self)
                self.owner = player
                print(f"{player.name} a acheté {self.name}. Il reste {player.money}€.")
            elif choice == "1":
                print(f"{player.name} n'a pas assez d'argent pour acheter {self.name}.")
        else:
            if self.owner != player:
                print(f"{player.name} arrive sur {self.name}, appartenant à {self.owner.name}.")
                print([p for p in self.sister if p.owner == self.owner])
                print(self.sister)
                rent = dice * (4 if len([p for p in self.sister if p.owner == self.owner]) == 1 else 10)
                if player.money >= rent:
                    player.money -= rent
                    self.owner.money += rent
                    print(f"{player.name} paie {rent}€ de loyer à {self.owner.name}. Solde restant : {player.money}€.")
                else:
                    print(f"{player.name} n'a pas assez d'argent pour payer le loyer !")
                    player.faillite()
            else:
                print(f"{player.name} arrive sur {self.name}.")


class Gare(Property):
    '''
        Classe Gare, héritant de Property, représentant une gare.
    '''
    def __init__(self, name, cost, rent, col):
        super().__init__(name, cost, rent)
        self.name = name
        self.cost = cost
        self.rent = rent
        self.col = col

    def action(self, player):
        if self.owner is None:
            print(f"{player.name} arrive sur {self.name}, coût : {self.cost}€, loyer : {self.rent}€.")
            print("1. Acheter")
            print("2. Ne rien faire")
            choice = input("Que voulez-vous faire ? (1/2) ")
            if choice == "1" and player.money >= self.cost:
                player.money -= self.cost
                player.properties.append(self)
                self.owner = player
                print(f"{player.name} a acheté {self.name}. Il reste {player.money}€.")
            elif choice == "1":
                print(f"{player.name} n'a pas assez d'argent pour acheter {self.name}.")
        else:
            if self.owner != player:
                print([p for p in self.sister if p.owner == self.owner])
                print(f"{player.name} arrive sur {self.name}, appartenant à {self.owner.name}.")
                rent = self.rent * len([p for p in self.sister if p.owner == self.owner])
                if player.money >= rent:
                    player.money -= rent
                    self.owner.money += rent
                    print(f"{player.name} paie {rent}€ de loyer à {self.owner.name}. Solde restant : {player.money}€.")
                else:
                    print(f"{player.name} n'a pas assez d'argent pour payer le loyer !")
                    player.faillite()
            else:
                print(f"{player.name} arrive sur {self.name}.")

class Jail(Tile):
    '''
        Classe Jail, héritant de Tile, représentant la prison.
    '''
    def __init__(self, name, tile_type):
        super().__init__(name, "jail")
        self.tile_type = tile_type
        self.name = name
    
    def action(self, player):
        if not player.prisonier[0] and player.position == 30:
            print(f"{player.name} arrive sur {self.name}.")
            player.prisonier[0] = True
            print("1. Utiliser une carte sortie de prison")
            print("2. Attendre 3 tours")
            choice = input("Que voulez-vous faire ? (1/2) ")
            while choice not in ("1", "2"):
                print("Veuillez entrer un choix valide.")
                choice = input("Que voulez-vous faire ? (1/2) ")
            if choice == "1" and player.money >= 50:
                player.money -= 50
                player.prisonier[0] = True
                print(f"{player.name} a payé 50€ pour sortir de prison.")
                player.prisonier[1] = 0
                player.position = 10
                player.prisonier[0] = False
                return
            elif choice == "1":
                print(f"{player.name} n'a pas assez d'argent")
            elif choice == "2":
                print(f"{player.name} attend son tour.")
            player.prisonier[1] += 1
        else:
            if player.prisonier[1] == 3:
                print(f"{player.name} est en prison depuis 3 tours, il doit payer \
                50€ pour sortir de prison.")
                if player.money >= 50:
                    player.money -= 50
                    player.prisonier[0] = False
                    player.prisonier[1] = 0
                    print(f"{player.name} a payé 50€ pour sortir de prison.")
                    player.position = 10
                else:
                    print(f"{player.name} n'a pas assez d'argent.")
                    player.faillite()
                    # Gestion de la faillite pourrait être ajoutée ici
            else:
                print(f"{player.name} est en prison depuis {player.prisonier[1]} tours.")
                player.prisonier[1] += 1


class Taxe(Tile):
    '''
        Classe Taxe, héritant de Tile, représentant une case de taxe.
    '''
    def __init__(self, name, tax):
        super().__init__(name, "tax")
        self.name = name
        self.taxe = tax

    def action(self, player):
        print(f"{player.name} arrive sur {self.name}.")
        if player.money >= self.taxe:
            player.money -= self.taxe
            print(f"{player.name} paie {self.taxe}€ de taxe. Solde restant : {player.money}€.")
        else:
            print(f"{player.name} n'a pas assez d'argent pour payer la taxe !")
            player.faillite()
            # Gestion de la faillite pourrait être ajoutée ici
