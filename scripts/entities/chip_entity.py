from entities.entity import Entity
from enums import ChipStates


class ChipEntity(Entity):
    def __init__(self, name, sprite, position, group, state=ChipStates.IDLE, spells=[]):
        super().__init__(name, sprite, position, group)
        self.state = state
        self.spells = spells
        self.active_spell = spells[0]
        self.delete_on_complete = False

    def activate(self, battler):
        if self.state == ChipStates.IDLE:
            self.state = ChipStates.RUNNING

            self.group.append(self)
            self.position.map = battler.position.map
            self.position.world = battler.position.world
            self.sprite.animation.play()

            for spell in self.spells:
                spell.position = self.position

                spell.run()
                self.active_spell = spell

    def update(self):
        if self.state == ChipStates.RUNNING:
            if self.sprite.animation.finished:
                self.state = ChipStates.FINISHED
        elif self.state == ChipStates.FINISHED:
            self.state = ChipStates.IDLE
            self.group.remove(self)

            if self.delete_on_complete:
                del self