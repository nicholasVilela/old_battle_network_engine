import pygame
import sys


class Game:
    def __init__(self, _screen, _scenes, _entry_scene):
        self.running = False

        self.screen = _screen
        self.clock = pygame.time.Clock()
        self.fps_text = ''

        self.scenes = _scenes
        self.entry_scene = _entry_scene
        self.scene_stack = [self.scenes[self.entry_scene]]
        self.active_scene = self.scene_stack[-1]

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
        pass


    def render(self):
        pass