from tkinter import *


class Gui:
    def __init__(self, player1_name: str, player2_name: str):
        self.cols = int(4)
        self.lines = int(3)
        self.player1_name: str = player1_name
        self.player2_name: str = player2_name
        self.root = Tk()
        print("gui created")

    def generate_grid(self, parent):
        for line in range(self.lines):
            for col in range(self.cols):
                Canvas(parent, width=60, height=60, background='ivory').grid(row=line, column=col)

    # bottom panel
    def create_bottom_panel(self):
        bottom_panel = Frame(self.root, padx=20, height=100)
        bottom_panel.pack(side='bottom', fill='both')

        Button(bottom_panel, text="Quit", command=self.root.destroy).grid(column=1, row=0)  # Création et placement d'un bouton

    # left panel
    def create_left_panel(self):
        left_panel = Frame(self.root, padx=30, pady=30, width=400)
        left_panel.pack(side='left', fill='both', expand=True)

        l_adversary_board = Frame(left_panel, width=100)
        l_adversary_board.pack()
        self.generate_grid(l_adversary_board)
        Label(left_panel, text="Adversary board").pack()

        l_player_board = Frame(left_panel, width=100)
        l_player_board.pack()
        self.generate_grid(l_player_board)
        Label(left_panel, text="Your board").pack()

        Label(left_panel, text=self.player1_name).pack()
        Label(left_panel, text="Enter coordinates : ").pack(side='left')
        Entry(left_panel).pack(side='right')

    # right panel
    def create_right_panel(self):
        right_panel = Frame(self.root, padx=30, pady=30, width=400)
        right_panel.pack(side='right', fill='both', expand=True)

        r_adversary_board = Frame(right_panel, width=100)
        r_adversary_board.pack()
        self.generate_grid(r_adversary_board)
        Label(right_panel, text="Adversary board").pack()

        r_player_board = Frame(right_panel, width=100)
        r_player_board.pack()
        self.generate_grid(r_player_board)
        Label(right_panel, text="Your board").pack()

        Label(right_panel, text=self.player2_name).pack()
        Label(right_panel, text="Enter coordinates : ").pack(side='left')
        Entry(right_panel).pack(side='right')

    # Construction et exécution de la fenêtre principale
    def generate_gui(self):
        self.root.title('Bataille navale !')
        self.create_bottom_panel()
        self.create_left_panel()
        self.create_right_panel()
        self.root.mainloop()  # Lancement de la «boucle principale»

    # def update_gui(self):
    #     self.root.
