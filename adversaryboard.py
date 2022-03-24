class AdversaryBoard:

    def __init__(self, dimension: tuple):
        self.board_dict: dict = self.create_dict(dimension)
        self.ships_destroyed: set = set()
        self.positions_fired_on: list = []

    def create_dict(self, dimension: tuple):
        board_dict = dict()
        for x in range(1, dimension[0] + 1):
            for y in range(1, dimension[1] + 1):
                board_dict[(x, y)] = "~~~~~"
        # print("matrix board : " + str(matrix))
        return board_dict

    def write_shot_result(self, coord: tuple, result: bool):
        if result:
            self.ships_destroyed.add(coord)
            self.board_dict[coord] = "coule"
            result = True
        else:
            self.board_dict[coord] = "plouf"
            result = False
        self.positions_fired_on.append(coord)
        return result
