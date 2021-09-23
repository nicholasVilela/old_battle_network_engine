import pygame

from game import Game
from resources import resources


pygame.init()
pygame.display.set_caption(resources['config'].title)

screen = pygame.display.set_mode((resources['config'].window.width, resources['config'].window.width))

game = Game(screen)
game.run()