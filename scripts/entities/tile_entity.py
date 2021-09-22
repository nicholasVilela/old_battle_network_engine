from entities.entity import Entity


class TileEntity(Entity):
    def __init__(self, name, sprite, position, group, battler=None):
        super().__init__(name, sprite, position, group)
        self.battler = battler