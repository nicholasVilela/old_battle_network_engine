from components.component import Component

from vec2 import Vec2
from enums import ComponentTypes


class PositionComponent(Component):
    def __init__(self, grid=Vec2(0, 0), world=Vec2(0, 0), offset=Vec2(0, 0)):
        super().__init__()
        self.name = ComponentTypes.POSITION
        self.grid = grid
        self.world = world
        self.offset = offset