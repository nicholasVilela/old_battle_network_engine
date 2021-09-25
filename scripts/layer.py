from util import create_surface
from vec2 import Vec2
from resources import resources
from const import COLORS


class Layer:
    def __init__(self, sprites=[]):
        self.surface = create_surface(Vec2(resources['config'].window.width, resources['config'].window.height), COLORS['black'])
        self.sprites = sprites

    def update(self):
        self.surface.fill(COLORS['black'])

        for sprite in self.sprites:
            self.surface.blit(sprite, (0, 0))