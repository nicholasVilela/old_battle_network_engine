import pygame

from rgb import RGB
from vec2 import Vec2


class Sprite:
    def __init__(self, path, layer, size=Vec2(0, 0), scale=1, tint=RGB(255, 255, 255)):
        self.path = path
        self.layer = layer
        self.size = size
        self.scale = scale
        self.tint = tint

        self.image = self.load_image()
        self.image.fill((self.tint.r, self.tint.g, self.tint.b), special_flags=pygame.BLEND_MULT)

        self.display = self.load_display()

    def render(self, position):
        self.layer.blit(self.display, (position.world.x + position.offset.x, position.world.y + position.offset.y))

    def load_image(self):
        return pygame.image.load(self.path).convert_alpha()

    def load_display(self):
        return pygame.transform.scale(self.image, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))