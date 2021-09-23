from enums import SceneStates
from resources import resources
from const import COLORS


class BaseScene:
    def __init__(self, name, controller, state=SceneStates.IDLE):
        self.name = name
        self.state = state
        self.layers = self.init_layers()
        self.entities = self.init_entities()
        self.controller = controller

    def update(self):
        for key in self.entities:
            for entity in self.entities[key]:
                entity.update()

    def get_event(self, event):
        pass

    def render(self, screen):
        if self.state == SceneStates.ACTIVE:
            for key in self.layers:
                self.layers[key].fill(COLORS['black'])

                for key in self.entities:
                    for entity in self.entities[key]:
                        entity.render()

            for key in self.layers:
                screen.blit(self.layers[key], (0, 0))
                
        # if self.state == SceneStates.ACTIVE:
        #     for key in self.layers:
        #         self.layers[key].fill(COLORS['black'])

        #     for key in self.entities:
        #         for entity in self.entities[key]:
        #             entity.render()

        # for key in self.layers

    def init_entities(self):
        return {}

    def init_layers(self):
        return {}

    def change_state(self, target_state):
        if self.state == target_state:
            return

        self.state = target_state