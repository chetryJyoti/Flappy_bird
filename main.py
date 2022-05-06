import random
import sys #for exiting the program we will use sys.exit
import pygame
from pygame.locals import * #pygame import

#global variables
FPS = 32
#For phone screen 
SCREENWIDTH = 289
SCREENHEIGHT= 511

SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=SCREENHEIGHT*0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER='/gallery/sprites/bird.png'
BACKGROUND='/gallery/sprites/background.png'
PIPE='/gallery/sprites/pipe.png'

# start point of game
if __name__ == "__main__":
    # initializes all pygame modules
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("Flappy bird by Coder_Chetz")
    # all numbers images
    GAME_SPRITES['numbers']=(
        pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/8.png').convert_alpha(),
    )
    


