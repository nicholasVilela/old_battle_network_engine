import pygame
import sys

from enums import SceneStates
from const import COLORS
from resources import resources


class Game:
    def __init__(self, _screen, _scenes, _entry_scene):
        self.running = False

        self.screen = _screen
        self.clock = pygame.time.Clock()
        self.fps_text = ''

        self.scenes = _scenes
        self.entry_scene = _entry_scene
        resources['scene_stack'] = [self.scenes[self.entry_scene]]
        self.active_scene = resources['scene_stack'].pop()
        self.active_scene.state = SceneStates.ACTIVE

    def run(self):
        self.running = True

        while self.running:
            self.update()
            self.render()

            pygame.display.update()

    def quit(self):
        pygame.quit()
        sys.exit()


    def update(self):
        self.update_events()
        self.update_scene()

    def update_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quit()

            self.active_scene.get_event(event)

    def update_scene(self):
        if self.active_scene.state == SceneStates.FINISHED:
            self.next_scene()

        self.active_scene.update()


    def next_scene(self):
        resources['scene_stack'] = resources['scene_stack'][:-1]
        self.active_scene = resources['scene_stack'].pop()
        self.active_scene.change_state(SceneStates.RUNNING)


    def render(self):
        self.screen.fill(COLORS['dim_gray'])
        self.render_scene()

    def render_scene(self):
        self.active_scene.render()

        for key in self.active_scene.layers:
            self.screen.blit(self.active_scene.layers[key], (0, 0))