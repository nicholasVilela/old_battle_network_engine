from entities.entity import Entity
from util import check_position, map_to_world
from enums import LivingStates, Stats, PlayerAnimations


class LivingEntity(Entity):
    def __init__(self, name, sprite, position, group, team, stats, state=LivingStates.SPAWN, chips=[]):
        super().__init__(name, sprite, position, group)
        self.team = team
        self.stats = stats
        self.state = state
        self.chips = chips

    def update(self):
        self.check_alive()

    def check_alive(self):
        if self.stats[Stats.HP].value <= 0:
            self.delete()

    def change_state(self, target_state, target_animation):
        if self.state == target_state:
            return

        self.state = target_state
        self.change_animation(target_animation)

    def change_animation(self, target_animation):
        self.sprite.change_animation(target_animation)

    def change_position(self, target_position):
        is_valid = check_position(target_position, self.team)

        if is_valid:
            self.change_state(LivingStates.MOVING, PlayerAnimations.MOVING)
            self.position.map = target_position
            self.position.world = map_to_world(self.position.map, self.sprite.scale)

    def delete(self):
        self.group.remove(self)