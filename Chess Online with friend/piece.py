import pygame

class Piece:
  def __init__(self, img):
    self.img = pygame.image.load(img)
    
  def get_piece(self):
    return self.img
