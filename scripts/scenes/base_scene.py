from enums import SceneStates


class BaseScene:
    def __init__(self, _state=SceneStates.IDLE):
        self.state = _state
        self.layers = self.init_layers()

    def update(self):
        pass

    def get_event(self, event):
        pass

    def render(self):
        pass

    def init_layers(self):
        return {}