from piece import Bishop
from piece import King
from piece import Rook
from piece import Pawn
from piece import Queen
from piece import Knight

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.board = [[0 for x in range(8)] for _ in range(rows)]


       
         # Black figures
        self.board[0][0] = Rook(0,0, "black")
        self.board[0][1] = Knight(0,1, "black")
        self.board[0][2] = Bishop(0,2, "black")
        self.board[0][3] = Queen(0,3, "black")
        self.board[0][4] = King(0,4, "black")
        self.board[0][5] = Bishop(0,5, "black")
        self.board[0][6] = Knight(0,6, "black")
        self.board[0][7] = Rook(0,7, "black")

      
        self.board[1][0] = Pawn(1,0, "black")
        self.board[1][1] = Pawn(1,1, "black")
        self.board[1][2] = Pawn(1,2, "black")
        self.board[1][3] = Pawn(1,3, "black")
        self.board[1][4] = Pawn(1,4, "black")
        self.board[1][5] = Pawn(1,5, "black")
        self.board[1][6] = Pawn(1,6, "black")
        self.board[1][7] = Pawn(1,7, "black")



        # white figures

        self.board[7][0] = Rook(7,0, "white")
        self.board[7][1] = Knight(7,1, "white")
        self.board[7][2] = Bishop(7,2, "white")
        self.board[7][3] = Queen(7,3, "white")
        self.board[7][4] = King(7,4, "white")
        self.board[7][5] = Bishop(7,5, "white")
        self.board[7][6] = Knight(7,6, "white")
        self.board[7][7] = Rook(7,7, "white")


        
        self.board[6][0] = Pawn(6,0, "white")
        self.board[6][1] = Pawn(6,1, "white")
        self.board[6][2] = Pawn(6,2, "white")
        self.board[6][3] = Pawn(6,3, "white")
        self.board[6][4] = Pawn(6,4, "white")
        self.board[6][5] = Pawn(6,5, "white")
        self.board[6][6] = Pawn(6,6, "white")
        self.board[6][7] = Pawn(6,7, "white")
        print(self.board)

    def draw(self, window):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(window)  


    def select(self, i, j):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False    
                             
        self.board[i][j].selected = True            