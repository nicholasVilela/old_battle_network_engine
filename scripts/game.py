import pygame
import sys

from enums import SceneStates, ButtonStates, Scenes
from const import COLORS
from config import FPS
from util import push_scene
from resources import resources


class Game:
    def __init__(self, screen, entry_scene):
        self.running = False

        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps_text = ''

        self.entry_scene = entry_scene
        resources['scene_stack'] = [resources['scenes'][self.entry_scene]]
        self.active_scene = resources['scene_stack'][-1]
        self.active_scene.state = SceneStates.ACTIVE

    def run(self):
        self.running = True

        while self.running:
            dt = self.clock.tick(FPS)
            self.update(dt)
            self.render()

            pygame.display.update()

    def quit(self):
        pygame.quit()
        sys.exit()


    def update(self, dt):
        resources['dt'] = dt
        self.active_scene = resources['scene_stack'][-1]

        self.update_events()
        self.update_controller()
        self.update_scene()

    def update_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quit()

            resources['controller'].update_event(event)

            self.active_scene.get_event(event)

    def update_scene(self):
        if self.active_scene.state == SceneStates.FINISHED:
            self.next_scene()

        self.active_scene.update()

    def update_controller(self):
        resources['controller'].update()

        if resources['controller'].start.state == ButtonStates.PRESSED:
            if self.active_scene.name == Scenes.PAUSE:
                resources['scene_stack'].pop()
            else:
                push_scene(Scenes.PAUSE)


    def next_scene(self):
        resources['scene_stack'] = resources['scene_stack'][:-1]
        self.active_scene = resources['scene_stack'][-1]
        self.active_scene.change_state(SceneStates.ACTIVE)


    def render(self):
        self.screen.fill(COLORS['dim_gray'])
        self.render_scene()

    def render_scene(self):
        self.active_scene.render()

        for scene in resources['scene_stack']:
            for key in scene.layers:
                self.screen.blit(scene.layers[key], (0, 0))