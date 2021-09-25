from entities.entity import Entity


class BattlerEntity(Entity):
    def __init__(self, name, components, group, team, state):
        super().__init__(name, components, group)
        self.team = team
        self.state = state

    def update(self):
        super().update()

    def set_state(self, state):
        if state != self.state:
            self.state = state