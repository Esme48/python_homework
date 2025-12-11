

class TictactoeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Board:
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

        self.valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
        
    def __str__(self):
        lines=[]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
print(Board())


# Notes: 
# - https://stackoverflow.com/questions/65729276/when-creating-lists-it-seems-that-forms-like-false-3-3-only-copies-the
# - https://www.geeksforgeeks.org/python/python-matrix/