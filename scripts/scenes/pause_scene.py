import pygame

from scenes import base_scene
from enums import SceneStates, Scenes
from resources import resources
from util import create_surface
from vec2 import Vec2
from const import COLORS, FONTS


class PauseScene(base_scene.BaseScene):
    def __init__(self, *args):
        super().__init__(*args)
        self.font = pygame.font.Font(FONTS['base'], 25)
        self.text = self.font.render('PAUSED', 1, COLORS['white'])

    def render(self):
        super().render()

        resources['scenes'][Scenes.BATTLE].render()

        self.layers['base'].blit(self.text, (200, 220))

    def init_layers(self):
        return {
            'base': create_surface(Vec2(resources['config'].window.width, resources['config'].window.height), COLORS['black']),
        }