from components.component import Component

from enums import ComponentTypes
from const import SPRITES

import pygame
import yaml


class SpriteComponent(Component):
    def __init__(self, sprite_path, config_path):
        super().__init__()
        self.name = ComponentTypes.SPRITE
        self.sprite_path = sprite_path
        self.config_path = config_path
        self.config = self.load_config()

        self.frame = 0
        self.scale = 1

        self.image = self.load_image()
        self.display = self.load_display()

    def update(self):
        self.display = self.load_display()

    def load_image(self):
        return pygame.image.load(self.sprite_path)

    def load_display(self):
        display = pygame.Surface((self.config.size[0], self.config.size[1])).convert_alpha()
        display.blit(self.image, (0, 0), (self.config.size[0] * self.frame, 0, 64, 64))

        return pygame.transform.scale(display, (display.get_width() * self.scale, display.get_height() * self.scale))

    def load_config(self):
        with open(self.config_path) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

            config = SpriteConfig(data['sprite_config'])

        return config

class SpriteConfig:
    def __init__(self, data):
        self.size = data['size']
        self.frames = [frame['frame_config'] for frame in data['frames']]
        self.frame_duration = data['frame_duration']
        self.loop = data['loop']