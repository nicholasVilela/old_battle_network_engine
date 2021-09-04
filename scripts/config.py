import pygame

from controller import Controller
from button import Button


WINDOW = {
    'width': 480,
    'height': 480,
}

MAP = {
    'width': 6,
    'height': 4,
}

TILE = {
    'width': 40,
    'height': 30,
    'surface_width': 40,
    'surface_height': 25,
}

CONTROLLER = Controller(
    up=Button(pygame.K_UP),
    down=Button(pygame.K_DOWN),
    left=Button(pygame.K_LEFT),
    right=Button(pygame.K_RIGHT),
    b=Button(pygame.K_z),
    start=Button(pygame.K_RETURN),
)

FPS = 144