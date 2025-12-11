

class TictactoeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Board:
    def __init__(self):
        self.board_array = [["" for _ in range(3)] for _ in range(3)]
        

game_board = Board()
print(f"This is the ouput: {game_board}")


# Notes: 
# - https://stackoverflow.com/questions/65729276/when-creating-lists-it-seems-that-forms-like-false-3-3-only-copies-the
