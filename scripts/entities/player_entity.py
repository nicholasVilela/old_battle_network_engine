from copy import copy

from entities.living_entity import LivingEntity
from enums import ButtonStates, Scenes, LivingStates
from util import push_scene
from resources import resources


class PlayerEntity(LivingEntity):
    def __init__(self, name, sprite, position, group, team, state, hp):
        super().__init__(name, sprite, position, group, team, state, hp)
 
    def update(self):
        self.update_state()
        self.update_input()

    def update_state(self):
        if self.state != LivingStates.IDLE and self.sprite.animation.finished:
            self.change_state(LivingStates.IDLE, LivingStates.IDLE)

    def update_input(self):
        self.update_movement()

    def update_movement(self):
        controller = resources['controller']
        target_position = copy(self.position.map)

        if self.state != LivingStates.IDLE:
            return

        if controller.up.state == (ButtonStates.PRESSED or ButtonStates.HOLDING):
            target_position.y -= 1
        elif controller.down.state == (ButtonStates.PRESSED or ButtonStates.HOLDING):
            target_position.y += 1
        elif controller.left.state == (ButtonStates.PRESSED or ButtonStates.HOLDING):
            target_position.x -= 1
        elif controller.right.state == (ButtonStates.PRESSED or ButtonStates.HOLDING):
            target_position.x += 1

        if target_position != self.position.map:
            self.change_position(target_position)