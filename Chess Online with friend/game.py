import pygame
import os
from piece import Bishop
from board import Board


DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = os.path.join(DIR, "img")

board = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "board_alt.png")), (750, 750))
rect = (113, 113, 525, 525)

def draw_gameWindow():
    global window, bo 

    window.blit(board, (0,0))
    bo = Board(8, 8) # 8 X 8

    bo.draw(window, bo.board)
    

   
    pygame.display.update()


def clickOnFigure(pos):

    """
    :return: pos (x, y) in range 0-7 0-7
    
    """

    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[0]
            i = int(divX / (rect[2] / 8)) 
            j = int(divY / (rect[3] / 8)) 
            print(i, j)


def main():

    global bo
    bo = Board(8, 8)
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
                pos = pygame.mouse.get_pos()
                i, j = clickOnFigure(pos);
                bo.select(i, j)




width = 750
height = 750     
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess in PyGame")
main()
