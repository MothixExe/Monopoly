import random

from Board import Board
from Player import Player
from Tirage import Tirage

class Game:
    '''
    Classe Game:
    - players: list, la liste des joueurs
    - board: Board, le plateau de jeu
    - current_player_index: int, l'index du joueur actuel
    '''
    def __init__(self):
        self.players = []
        self.board = Board()
        Tirage.Monopoly = self
        self.current_player_index = 0

    def setup_game(self):
        '''
        Démarrage du jeu : initialisation des joueurs et détermination de l'ordre de jeu.
        '''
        print("=== BIENVENUE AU JEU DE MONOPOLY ===")
        print("Qu'elle pion voulez-vous choisir ?")
        print("1. Chien")
        print("2. Chapeau")
        print("3. Bateau")
        print("4. Voiture")
        print("5. Fer à cheval")
        print("6. Chaussure")
        print("7. Canon")
        print("8. Dé à coudre")
        print("9. Chariot")

        num_players = int(input("Combien de joueurs vont jouer ? (2-8) "))
        while num_players < 2 or num_players > 8:
            num_players = int(input("Veuillez entrer un nombre de joueurs entre 2 et 8 : "))

        for i in range(num_players):
            name = input(f"Entrez le nom du joueur {i + 1} : ")
            self.players.append(Player(name))

        # Déterminer l'ordre de jeu
        print("\n=== JET DE DÉ POUR DÉTERMINER L'ORDRE ===")
        rolls = {}
        for player in self.players:
            roll = random.randint(1, 6)
            print(f"{player.name} lance les dés et obtient {roll}.")
            rolls[player] = roll

        self.players.sort(key=lambda p: rolls[p], reverse=True)
        print("\n=== ORDRE DE JEU ===")
        for i, player in enumerate(self.players):
            print(f"{i + 1}. {player.name} (Solde : {player.money}€)")

    def play_turn(self):
        '''
        Méthode play_turn:
        Gère le tour d'un joueur.
        '''
        player = self.players[self.current_player_index]

        i = 0
        while True:  # Rejouer si un jet pair
            print(f"\n=== TOUR DE {player.name} ===")
            print(f"Solde : {player.money}€")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice_total = dice1 + dice2
            print(f"\n{player.name} lance les dés et obtient : {dice_total}")
            if not player.prisonier[0]:
                player.move(dice_total, len(self.board.tiles))

            current_tile = self.board.tiles[player.position]

            if current_tile.col == "compagnie":
                current_tile.action(player, dice_total)
            else:
                current_tile.action(player)

            # Rejouer si le jet est pair
            # Si 3 doubles consécutifs, le joueur va en prison
            if dice1 == dice2 and not player.prisonier[0]:
                print(f"{player.name} a obtenu un chiffre pair et peut rejouer.")
                i += 1
            elif i == 3:
                print(f"{player.name} a obtenu 3 doubles consécutifs et va en prison.")
                player.position = 30
                current_tile = self.board.tiles[player.position]
                current_tile.action(player)
            else:
                break

        input("Appuyez sur Entrée pour continuer...")

        # Passer au joueur suivant
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def display_board(self):
        '''
        Méthode display_board:
        Affiche le plateau de jeu.
        '''
        self.board.display(self.players)

    def start_game(self):
        '''
        Méthode start_game:
        Démarre le jeu.
        '''
        self.setup_game()
        while True:  # Boucle principale du jeu
            self.play_turn()
            self.display_board()


# Lancer le jeu
if __name__ == "__main__":
    game = Game()
    game.start_game()