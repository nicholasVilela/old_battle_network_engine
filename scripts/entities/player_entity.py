from entities.living_entity import LivingEntity
from enums import ButtonStates, Scenes
from util import push_scene
from resources import resources


class PlayerEntity(LivingEntity):
    def __init__(self, name, sprite, position, group, team, state, hp):
        super().__init__(name, sprite, position, group, team, state, hp)

    def update(self):
        self.update_input()
        self.update_state()

    def update_input(self):
        controller = resources['controller']
        controller.update()

        if controller.start.state == ButtonStates.PRESSED:
            push_scene(Scenes.PAUSE)

    def update_state(self):
        pass