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

game = Game()
print(f"Current turn: {game.turn}")
print(f"Is it a tie? {game.tie}")
print(f"Winner: {game.winner}")
print(f"Board: {game.board}")