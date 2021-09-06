import pygame

from rgb import RGB
from vec2 import Vec2
from const import SPRITES
from enums import LivingStates


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


class AnimatedSprite:
    def __init__(self, path, layer, size, scale, tint=RGB(255, 255, 255), animations={}, entry_animation=LivingStates.SPAWN):
        self.animations = animations
        self.animation = self.animations[entry_animation]

        self.path = path
        self.layer = layer
        self.size = size
        self.scale = scale
        self.tint = tint
        self.images = self.load_images()
        self.image = self.load_image()
        self.display = self.load_display()

    def render(self, position):
        self.animation.update()
        self.display = self.load_display()
        self.layer.blit(self.display, (position.world.x + position.offset.x, position.world.y + position.offset.y))

    def load_images(self):
        images = {}
        for animation_name in self.animations:
            images[animation_name] = pygame.image.load(self.path[animation_name]).convert_alpha()

        return images

    def load_image(self):
        return self.images[self.animation.name]

    def load_display(self):
        display = pygame.Surface((self.size.x, self.size.y)).convert_alpha()
        display.blit(self.image, (0, 0), (self.size.x * self.animation.frame, 0, 64, 64))

        return pygame.transform.scale(display, (display.get_width() * self.scale, display.get_height() * self.scale))

    def change_animation(self, target_animation):
        self.animation.finished = False
        self.animation = self.animations[target_animation]
        self.image = self.load_image()
        self.animation.play()