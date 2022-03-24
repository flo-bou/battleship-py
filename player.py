from numbers import Number
import game
from personalboard import *
from adversaryboard import *


class Player:

    def __init__(self, name: str, board_dimension: tuple):
        self.name: str = name
        self.board_dimension: tuple = board_dimension
        self.personal_board = PersonalBoard(board_dimension)
        self.adversary_board = AdversaryBoard(board_dimension)
        self.isDead: bool = False


    def shoot(self):
        loop: bool = True
        scan: str
        fire_coord: tuple
        # print("Your board :")
        # self.display_board(self.personal_board.board_dict)
        # print()
        print("You still have " + str(self.personal_board.ships_remaining) + " ships.")
        print("Your ennemy board :")
        self.display_board(self.adversary_board.board_dict)
        print()

        while loop:
            scan = input(self.name + ", sur quelle position voulez-vous tirer ? [x,y] :")
            fire_coord = self.from_str_to_tuple(scan)
            loop = fire_coord == False
        # l'envoyer au board du player adverse, ici dans une variable statique de game
        game.shot_coord = fire_coord


    def receive_shoot(self):
        # test pour savoir si la coordonnée touche
        # réception du résultat depuis la variable statique
        shot_coord: tuple = game.shot_coord
        # notation du résultat dans personnal board
        result: bool = self.personal_board.is_ennemy_shot_successful(shot_coord)
        # mise à jour de l'IHM (avec validation)
        # renvoi de la réponse
        return result


    def write_result(self, result: bool):
        self.adversary_board.write_shot_result(game.shot_coord, result)
        if result:
            print("*** Vous avez touché ! ***")
        else:
            print("~~~ Plouf ! Pas de chance. ~~~")
        # mise à jour de l'IHM (avec validation)

    # return correct tuple or False for bad inputs
    def from_str_to_tuple(self, coord_str: str):
        liste: list = coord_str.split(",")
        liste2: list = []
        result = True

        for entry in liste:
            liste2.append(entry.strip())
        try:
            result = int(liste2[0]), int(liste2[1])
            if not (result[0] <= self.board_dimension[0] and result[1] <= self.board_dimension[1]):
                result = False
        except ValueError:
            result = False
        if liste2.__len__() != 2:
            result = False
        return result


    def display_board(self, board_dict: dict):
        for y in range(1, int(self.board_dimension[1]) + 1):
            for item in board_dict:
                if item[1] == y:
                    print(board_dict[item], end=" ")
            print()


    def is_dead(self):
        return not (self.personal_board.ships_remaining == set())
