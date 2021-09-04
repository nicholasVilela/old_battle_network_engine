from vec2 import Vec2


class Position:
    def __init__(self, _map=Vec2(0, 0), _world=Vec2(0, 0)):
        self.map = _map
        self.world = _world