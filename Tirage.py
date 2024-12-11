'''
Classe Tirage héritant de Tile, représentant une case de tirage. (Caisse de Communauté ou Chance)
'''
import random
from Tile import Tile

class Tirage(Tile):
    '''
    Classe Tirage héritant de Tile, représentant une case de tirage. (Caisse de Communauté ou Chance)
    '''

    Monopoly = None

    def __init__(self, name):
        super().__init__(name, "tirage")
        self.name = name
    
    def action(self, player):
        print(f"{player.name} arrive sur {self.name}.")
        if self.name == "Caisse de Communauté":
            cartes = [
                {"carte": "Avancez jusqu'à la case Départ. (Collectez 200 €)", "somme": 200, "move": 0},
                {"carte": "Erreur de la banque en votre faveur. Recevez 200 €", "somme": 200, "move": None},
                {"carte": "Frais de scolarité. Payez 150 €", "somme": -150, "move": None},
                {"carte": "Recevez votre revenu annuel. Collectez 100 €", "somme": 100, "move": None},
                {"carte": "C'est votre anniversaire. Chaque joueur doit vous donner 10 €", "somme": 10, "move": None},
                {"carte": "Payez une amende de 50 €", "somme": -50, "move": None},
                {"carte": "Vous avez gagné le deuxième prix de beauté. Recevez 10 €", "somme": 10, "move": None},
                {"carte": "Vous héritez de 100 €", "somme": 100, "move": None},
                {"carte": "Payez une amende de 10 € ou tirez une carte Chance", "somme": -10, "move": None},
                {"carte": "Allez en prison. Ne passez pas par la case Départ et ne recevez pas 200 €", "somme": 0, "move": 30},
                {"carte": "Libéré de prison gratuitement. Gardez cette carte jusqu'à ce qu'elle soit utilisée", "somme": 0, "move": None},
                {"carte": "Les réparations de votre propriété vous coûtent 40 € par maison et 115 € par hôtel", "somme": -40, "move": None},
                {"carte": "Recevez 25 € pour services rendus", "somme": 25, "move": None},
                {"carte": "Retournez à Belleville", "somme": 0, "move": 1},
                {"carte": "Retournez à la Gare de Lyon", "somme": 0, "move": 15},
                {"carte": "Vous avez gagné le concours de mots croisés. Recevez 100 €", "somme": 100, "move": None}
            ]
        else:
            cartes = [
                {"carte": "Avancez jusqu'à la case Départ. (Collectez 200 €)", "somme": 200, "move": 0},
                {"carte": "Avancez jusqu'à la Rue de la Paix", "somme": 0, "move": 39},
                {"carte": "Avancez jusqu'à l'Avenue Henri-Martin. Si vous passez par la case Départ, collectez 200 €", "somme": 200, "move": 24},
                {"carte": "Avancez jusqu'à la Gare de Lyon. Si vous passez par la case Départ, collectez 200 €", "somme": 200, "move": 15},
                {"carte": "Vous êtes imposé pour des réparations, 40 € par maison et 115 € par hôtel", "somme": -40, "move": None},
                {"carte": "Faites des réparations dans toutes vos propriétés : 25 € par maison, 100 € par hôtel", "somme": -25, "move": None},
                {"carte": "Amende pour excès de vitesse, payez 15 €", "somme": -15, "move": None},
                {"carte": "Payez une amende de 150 € ou tirez une carte caisse de communauté", "somme": -150, "move": None},
                {"carte": "Reculez de trois cases", "somme": 0, "move": None},
                {"carte": "Allez en prison. Ne passez pas par la case Départ et ne recevez pas 200 €", "somme": 0, "move": 10},
                {"carte": "Rendez-vous à la Gare de Lyon", "somme": 0, "move": 15},
                {"carte": "Votre immeuble et votre prêt rapportent. Vous devez recevoir 150 €", "somme": 150, "move": None},
                {"carte": "Avancez jusqu'à la case départ, collectez 200 €", "somme": 200, "move": 0},
                {"carte": "Recevez 100 € en héritage", "somme": 100, "move": None},
                {"carte": "Libéré de prison gratuitement. Gardez cette carte jusqu'à ce qu'elle soit utilisée", "somme": 0, "move": None},
                {"carte": "Vous avez gagné le concours de mots croisés. Recevez 100 €", "somme": 100, "move": None}
            ]
        carte = random.choice(cartes)
        print(carte["carte"])
        player.money += carte["somme"]
        if carte["move"] is not None:
            player.position = carte["move"]
            print(f"{player.name} se déplace jusqu'à la case {player.position}.")
            if carte["move"] == 10:
                player.get_current_tile(Tirage.Monopoly).action(player)
        print(f"{player.name} a maintenant {player.money}€ et est sur la case {player.position}.")