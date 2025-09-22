class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
            """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()

            if move in self.board:
                if self.board[move] is None:
                    return move
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid move! Please enter a position like a1, b2, c3, etc:")

    def check_winner(self):
        b = self.board

        # ROWS
        if b['a1'] and (b['a1'] == b['b1'] == b['c1']):
            self.winner = b['a1']
            return
        if b['a2'] and (b['a2'] == b['b2'] == b['c2']):
            self.winner = b['a2']
            return
        if b['a3'] and (b['a3'] == b['b3'] == b['c3']):
            self.winner = b['a3']
            return

        # COLUMNS
        if b['a1'] and (b['a1'] == b['a2'] == b['a3']):
            self.winner = b['a1']
            return
        if b['b1'] and (b['b1'] == b['b2'] == b['b3']):
            self.winner = b['b1']
            return
        if b['c1'] and (b['c1'] == b['c2'] == b['c3']):
            self.winner = b['c1']
            return

        # DIAGONALS
        if b['a1'] and (b['a1'] == b['b2'] == b['c3']):
            self.winner = b['a1']
            return
        if b['c1'] and (b['c1'] == b['b2'] == b['a3']):
            self.winner = b['c1']
            return

    def check_tie(self):
        board_full = all(space is not None for space in self.board.values())

        no_winner = self.winner is None

        if board_full and no_winner:
            self.tie = True

    def switch_turn(self):
        turn_lookup = {'X': 'O', 'O': 'X'}
        self.turn = turn_lookup[self.turn]

    def play_game(self):
        print("Welcome to Py-Pac-Poe!")
        print("Let's play!")
        self.render()


game_instance = Game()
print(f"Start: {game_instance.turn}")
game_instance.switch_turn()
print(f"Switch turn: {game_instance.turn}")
