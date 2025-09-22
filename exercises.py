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

    def play_game(self):
        print("Welcome to Py-Pac-Poe!")
        print("Let's play!")

game_instance = Game()
game_instance.play_game()

print(f"Current turn: {game_instance.turn}")
print(f"Is it a tie? {game_instance.tie}")
print(f"Winner: {game_instance.winner}")
print(f"Board: {game_instance.board}")