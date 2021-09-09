from copy import copy

from entities.living_entity import LivingEntity
from enums import ButtonStates, Scenes, LivingStates, PlayerAnimations, ChipStates
from util import push_scene, check_position
from resources import resources
from instruction import Instruction


class PlayerEntity(LivingEntity):
    def __init__(self, name, sprite, position, group, team, state, stats, chips):
        super().__init__(name, sprite, position, group, team, state, stats, chips)
 
    def update(self):
        self.update_state()
        self.update_input()

    def update_state(self):
        if self.state != LivingStates.IDLE and self.sprite.animation.finished:
            self.change_state(LivingStates.IDLE, PlayerAnimations.IDLE)

    def update_input(self):
        self.update_movement()
        self.update_attacks()

    def update_movement(self):
        if self.state != LivingStates.IDLE:
            return

        controller = resources['controller']
        target_position = copy(self.position.map)

        if controller.up.state == (ButtonStates.PRESSED or ButtonStates.HOLDING):
            target_position.y -= 1
        elif controller.down.state == (ButtonStates.PRESSED or ButtonStates.HOLDING):
            target_position.y += 1
        elif controller.left.state == (ButtonStates.PRESSED or ButtonStates.HOLDING):
            target_position.x -= 1
        elif controller.right.state == (ButtonStates.PRESSED or ButtonStates.HOLDING):
            target_position.x += 1

        if target_position != self.position.map:
            is_valid = check_position(target_position, self.team)
            if is_valid:
                self.sprite.animations[PlayerAnimations.MOVING].add_instruction(frame=3, function=self.change_position, params=[target_position])
                self.change_state(LivingStates.MOVING, PlayerAnimations.MOVING)

    def update_attacks(self):
        if self.state == LivingStates.IDLE:
            if len(self.chips) > 0 and resources['controller'].a.state == ButtonStates.PRESSED:
                chip = self.chips[-1]

                if chip.animation_type == PlayerAnimations.ATTACK_SHOOT_HEAVY:
                    self.sprite.animations[chip.animation_type].add_instruction(frame=3, function=chip.activate, params=[])
                    chip.sprite.animations[ChipStates.RUNNING].add_instruction(frame=7, function=chip.active_spell.check_if_hit, params=[])
                elif chip.animation_type == PlayerAnimations.ATTACK_SLASH:
                    self.sprite.animations[chip.animation_type].add_instruction(frame=2, function=chip.activate, params=[])
                    chip.sprite.animations[ChipStates.RUNNING].add_instruction(frame=1, function=chip.active_spell.check_if_hit, params=[])

                self.chips.pop()
                self.change_state(LivingStates.ATTACKING, chip.animation_type)