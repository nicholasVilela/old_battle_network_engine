from entities.entity import Entity
from util import check_position, map_to_world


class LivingEntity(Entity):
    def __init__(self, name, sprite, position, group, team, state, hp):
        super().__init__(name, sprite, position, group)
        self.team = team
        self.state = state
        self.hp = hp

    def update(self):
        self.check_alive()

    def check_alive(self):
        if self.hp <= 0:
            self.delete()

    def change_position(self, target_position):
        is_valid = check_position(target_position, self.team)

        if is_valid:
            self.position.map = target_position
            self.position.world = map_to_world(self.position.map, self.sprite.scale)

    def delete(self):
        self.group.remove(self)