from entities.entity import Entity
from enums import SpellTypes, SpellStates
from util import check_spell_position
from resources import resources


class SpellEntity(Entity):
    def __init__(self, name, sprite, position, group, state, _type, modifier, stat, affected, enemy_team):
        super().__init__(name, sprite, position, group)
        self.state = state
        self.type = _type
        self.modifier = modifier
        self.stat = stat
        self.affected = affected
        self.enemy_team = enemy_team

    def run(self):
        if self.state == SpellStates.IDLE:
            self.state = SpellStates.RUNNING
            self.group.append(self)

    def update(self):
        if self.state == SpellStates.FINISHED:
            self.delete()

    def check_if_hit(self):
        if self.type == SpellTypes.HITSCAN:
                for pos in self.affected:
                    tile_position = self.position.map + pos
                    is_valid = check_spell_position(tile_position)

                    if is_valid:
                        for entity in resources[self.enemy_team]:
                            if entity.position.map == tile_position:
                                self.on_hit(entity)

                self.state = SpellStates.FINISHED

    def on_hit(self, entity):
        entity.stats[self.stat].change(self.modifier)

    def delete(self):
        self.state = SpellStates.IDLE
        self.group.remove(self)