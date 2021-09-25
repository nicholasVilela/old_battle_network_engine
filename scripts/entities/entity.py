class Entity:
    def __init__(self, name, components, group):
        self.name = name
        self.components = components
        self.group = group

        self.set_parent(self)
        self.group.append(self)

    def update(self):
        for component in self.components:
            component.update()

    def add_component(self, component):
        if component not in self.components:
            self.components.append(component)

    def remove_component(self, component):
        if component in self.components:
            self.components.remove(component)

    def set_parent(self, parent):
        for component in self.components:
            component.parent = parent

# class Entity:
#     def __init__(self, name, sprite, position, group):
#         self.name = name
#         self.sprite = sprite
#         self.position = position
#         self.group = group

#     def update(self):
#         pass

#     def render(self):
#         if self.sprite != None:
#             self.sprite.render(self.position)