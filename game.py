import pygame
import sys
import os
from pygame.locals import *

pygame.init()  # initialize pygame
clock = pygame.time.Clock()
screenwidth, screenheight = (640,640)
screen = pygame.display.set_mode((screenwidth, screenheight))
bg = pygame.image.load(os.path.join("./", "background.png"))
pygame.mouse.set_visible(0)
pygame.display.set_caption("Space Age Game")  # fix indentation

class SnakeCharacter:
    def __init__(self, screenheight, screenwidth, imagefile):
        self.shape = pygame.image.load(imagefile)
        self.top = screenheight - self.shape.getheight()
        self.left = screenwidth/2 - self.shape.get_width()/2
    def Show(self, surface):
        surface.blit(self.shape)

while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()  # update screen
