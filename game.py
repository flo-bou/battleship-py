import player
nb_ship: int = 2
shot_coord: tuple


class Game:

    def __init__(self):
        self.board_dimension: tuple
        self.setup()
        self.player_1 = player.Player("Player 1", self.board_dimension)
        self.player_2 = player.Player("Player 2", self.board_dimension)
        print("Players created")

    def play(self):
        self.turn()
        self.end()

    def setup(self):
        print("------------BATTLESHIP!------------")
        board_str: str = input("Choose the board dimension [x,y] : ")
        self.board_dimension = self.from_str_to_tuple(board_str)
        print()

    def turn(self):
        compteur: int = 0
        result: bool
        current_player = self.player_1
        other_player = self.player_2
        while current_player.is_dead():
            compteur += 1
            print("----------" + current_player.name + "'s turn----------")
            current_player.shoot()
            result = other_player.receive_shoot()
            current_player.write_result(result)
            print("End of turn" + str(compteur))
            print()
            temp = current_player
            current_player = other_player
            other_player = temp
        print(current_player.name + " has no more ships.")
        print(other_player.name + " WINS !")


    def end(self):
        print("------------Endgame------------")
        print(self.player_1.name + "'s board :")
        self.player_1.display_board(self.player_1.personal_board.board_dict)
        print()

        print(self.player_2.name + "'s board :")
        self.player_2.display_board(self.player_2.personal_board.board_dict)
        print()


    def from_str_to_tuple(self, coord_str: str):
        liste: list = coord_str.split(",")
        liste2: list = []
        for entry in liste:
            liste2.append(int(entry.strip()))
        result: tuple = tuple(liste2)
        return result
