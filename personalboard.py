from game import nb_ship
from random import randint

class PersonalBoard:

    def __init__(self, dimension: tuple):
        self.board_dict: dict = self.create_dict(dimension)
        self.ships_destroyed: set = set()
        self.ships_remaining: set = self.create_ships(dimension)
        self.add_ships_to_board()
        self.positions_fired_on: list = []


    def create_dict(self, dimension: tuple):
        board_dict = dict()
        for x in range(1, dimension[0] + 1):
            for y in range(1, dimension[1] + 1):
                board_dict[(x, y)] = "~~~~~"
        return board_dict


    def create_ships(self, dimension: tuple):
        ships: set = set()
        while not (ships.__len__() == nb_ship):
            ship: tuple = randint(1, dimension[0]), randint(1, dimension[1])
            ships.add(ship)
        return ships


    def add_ships_to_board(self):
        for coord in self.ships_remaining:
            self.board_dict[coord] = "ship-"


    def is_ennemy_shot_successful(self, coord: tuple):
        # tester si la coord est dans ships remaining
        result: bool
        if coord in self.ships_remaining:
            self.ships_remaining.remove(coord)
            self.ships_destroyed.add(coord)
            self.board_dict[coord] = "coule"
            result = True
        else:
            self.board_dict[coord] = "plouf"
            result = False
        self.positions_fired_on.append(coord)
        return result
