class Entity:
    def __init__(self, name, sprite, position, group):
        self.name = name
        self.sprite = sprite
        self.position = position
        self.group = group

    def update(self):
        pass

    def render(self):
        if self.sprite != None:
            self.sprite.render(self.position)