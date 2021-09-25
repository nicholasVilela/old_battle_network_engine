from components.component import Component

from enums import ComponentTypes


class SpriteComponent(Component):
    def __init__(self, path):
        super().__init__()
        self.name = ComponentTypes.SPRITE
        self.path = path