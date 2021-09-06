from enums import SceneStates
from resources import resources
from const import COLORS
from config import CONTROLLER


class BaseScene:
    def __init__(self, name, state=SceneStates.IDLE):
        self.name = name
        self.state = state
        self.layers = self.init_layers()
        self.entities = self.init_entities()

    def update(self):
        for key in self.entities:
            for entity in self.entities[key]:
                entity.update()

    def get_event(self, event):
        pass

    def render(self):
        if self.state == SceneStates.ACTIVE:
            for key in self.layers:
                self.layers[key].fill(COLORS['black'])

            for key in self.entities:
                for entity in self.entities[key]:
                    entity.render()

    def init_entities(self):
        return {}

    def init_layers(self):
        return {}

    def change_state(self, target_state):
        if self.state == target_state:
            return

        self.state = target_state