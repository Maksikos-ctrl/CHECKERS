import pygame
import os
from piece import Bishop
from board import Board


DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = os.path.join(DIR, "img")

board = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "board_alt.png")), (750, 750))
rect = (113, 113, 525, 525)

def draw_gameWindow():
    global window

    window.blit(board, (0,0))
    bo = Board(8, 8) # 8 X 8

    bo.draw(window)
    

   
    pygame.display.update()



def main():
  
    

    clock  = pygame.time.Clock()
    run = True
    while run:
        clock.tick(10)

        draw_gameWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                    pass



width = 750
height = 750     
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess in PyGame")
main()
