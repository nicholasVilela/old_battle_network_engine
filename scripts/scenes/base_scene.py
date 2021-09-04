from enums import SceneStates
from resources import resources
from const import COLORS


class BaseScene:
    def __init__(self, state=SceneStates.IDLE):
        self.state = state
        self.layers = self.init_layers()
        self.entities = self.init_entities()

    def update(self):
        pass

    def get_event(self, event):
        pass

    def render(self):
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

    def push_scene(self, target_scene):
        resources['scene_stack'].append(target_scene)