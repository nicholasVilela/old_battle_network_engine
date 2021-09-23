import pygame
from pygame.locals import *
import sys
import yaml

from enums import SceneStates, ButtonStates, Scenes
from const import COLORS
from util import push_scene
from resources import resources
from controller import Controller

from scene_manager import SceneManager
from scenes import battle_scene, select_scene, pause_scene, end_scene

from broker import Broker


class Game:
    def __init__(self, screen):
        self.running = False

        self.screen = screen
        self.clock = pygame.time.Clock()

        self.controller = self.load_controller()
        self.scene_manager = self.load_scene_manager()

    def run(self):
        self.running = True

        while self.running:
            dt = self.clock.tick(resources['config'].fps)

            self.update(dt)
            self.render()

            pygame.display.update()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self, dt):
        resources['dt'] = dt

        self.update_events()
        self.update_controller()
        self.scene_manager.update()

    def update_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quit()

            self.controller.get_event(event)

            self.scene_manager.get_event(event)

    def update_controller(self):
        self.controller.update()
        pass
        # resources['controller'].update()

        # if resources['controller'].start.state == ButtonStates.PRESSED:
        #     if self.active_scene.name == Scenes.PAUSE:
        #         resources['scene_stack'].pop()
        #     else:
        #         push_scene(Scenes.PAUSE)

    def render(self):
        self.screen.fill(COLORS['dim_gray'])
        self.scene_manager.render(self.screen)

    def load_scene_manager(self):
        scenes = {
            Scenes.BATTLE: battle_scene.BattleScene(Scenes.BATTLE, self.controller),
            Scenes.SELECT: select_scene.SelectScene(Scenes.SELECT, self.controller),
            Scenes.PAUSE : pause_scene.PauseScene(Scenes.PAUSE, self.controller),
            Scenes.END   : end_scene.EndScene(Scenes.END, self.controller),
        }

        return SceneManager(
            scenes=scenes,
            entry_scene=Scenes.BATTLE,
        )

    def load_controller(self):
        with open('../config/controller.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

            return Controller(
                broker=resources['broker'],
                up=data['controller']['up'],
                down=data['controller']['down'],
                left=data['controller']['left'],
                right=data['controller']['right'],
                b=data['controller']['b'],
                a=data['controller']['a'],
                start=data['controller']['start']
            )