from components.component import Component
from enums import ComponentTypes


class MovementComponent(Component):
    def __init__(self):
        super().__init__()
        self.name = ComponentTypes.MOVEMENT