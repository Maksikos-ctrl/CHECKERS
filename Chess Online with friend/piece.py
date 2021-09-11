import pygame
import os


DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = os.path.join(DIR, "img")

b_bishop = pygame.image.load(os.path.join(IMG_DIR, "black_bishop.png"))
b_king = pygame.image.load(os.path.join(IMG_DIR, "black_king.png"))
b_knight = pygame.image.load(os.path.join(IMG_DIR, "black_knight.png"))
b_pawn = pygame.image.load(os.path.join(IMG_DIR, "black_pawn.png"))
b_queen = pygame.image.load(os.path.join(IMG_DIR, "black_queen.png"))
b_rook = pygame.image.load(os.path.join(IMG_DIR, "black_rook.png"))



w_bishop = pygame.image.load(os.path.join(IMG_DIR, "white_bishop.png"))
w_king = pygame.image.load(os.path.join(IMG_DIR, "white_king.png"))
w_knight = pygame.image.load(os.path.join(IMG_DIR, "white_knight.png"))
w_pawn = pygame.image.load(os.path.join(IMG_DIR, "white_pawn.png"))
w_queen = pygame.image.load(os.path.join(IMG_DIR, "white_queen.png"))
w_rook = pygame.image.load(os.path.join(IMG_DIR, "white_rook.png"))


black = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]

white = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]


B = []
W = []


for img in black:
    B.append(pygame.transform.scale(img, (55,65)))

for img in white:
    W.append(pygame.transform.scale(img, (55,55)))

class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, column, color):
      self.row = row
      self.column = column
      self.color = color
      self.selected = False
      
    def actual_moves(self):
      pass


    def is_selected(self):
      return self.selected

    def draw(self, win):
       if self.color == "white":  
           drawThis = W[self.img] 
       else:     
           drawThis = B[self.img] 


     
       
       x = 5 + round(self.startX + (self.column * self.rect[2] / 8))   # 8 X 8  
       y = 5 + round(self.startY + (self.row * self.rect[3] / 8))   

       if self.selected:    
           pygame.draw.rect(win, (255,0,0), (x, y, 55, 55), 2)  

       win.blit(drawThis, (x, y))




class Bishop(Piece):
    img = 0 

class King(Piece):
    img = 1  

    def actual_moves(self, board):
        r = self.row
        c = self.column

        moves = []

        # TOP LEFT
        if r < 7:
           if c > 0:
               moves.append((r-1, c-1))

        # Top middle
           moves.append((r-1, c))


        # Top right
           if c < 7:
            moves.append((r-1, c+1))   

            
            
        


class Knight(Piece):
    img = 2 

    def actual_moves(self, board):
        r = self.row
        c = self.column

        moves = []


        # down left
        if r < 6 and c > 0:
            p = board[r+2][c-1]
            if p == 0:
                moves.append((c-1, r+2)) 
        
        # up left
        if r > 1 and c > 0:
            p = board[r-2][c-1]
            if p == 0:
                moves.append((c-1, r-2)) 

        # down right
        if r < 6 and c < 7:
            p = board[r+2][c+1]
            if p == 0:
                moves.append((c+1, r+2))            

        # Up right 
        if r > 2 and c < 7:
            p = board[r-2][c+1]
        if p == 0:
            moves.append((c+1, r-2))               
                
        return moves     


class Pawn(Piece):
    img = 3 
    
    def __init__(self, row, col, color):
        super().__init__(row, col, color)  # The super() function returns an object that represents the parent class.
        self.first = True
        self.queen = False

    def actual_moves(self, board):
        r = self.row
        c = self.column

        moves = []

        if self.first:
            if r < 6: 
                p = board[r+1][c]
                if p == 0:
                    moves.append((c, c+2))

        if r < 7:
            p = board[r+1][c]
            if p == 0:
                moves.append((r, c+1)) 
                
        return moves                      
                    


class Queen(Piece):
    img = 4    

    def move(self, board):
        pass




class Rook(Piece):
    img = 5
 
