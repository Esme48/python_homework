

class TictactoeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Board:
    def __init__(self):
        self.board_array = [["" for _ in range(3)] for _ in range(3)]
        self.turn = "X"

        valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
        

game_board = Board()
print(f"This is the ouput: {game_board}")


# Notes: 
# - https://stackoverflow.com/questions/65729276/when-creating-lists-it-seems-that-forms-like-false-3-3-only-copies-the
# - https://www.geeksforgeeks.org/python/python-matrix/