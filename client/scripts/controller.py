from copy import copy


class Controller:
    def __init__(self, up, down, left, right, b, a, start):
        self.buttons = []

        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.b = b
        self.a = a
        self.start = start

        self.buttons.append(self.up)
        self.buttons.append(self.down)
        self.buttons.append(self.left)
        self.buttons.append(self.right)
        self.buttons.append(self.b)
        self.buttons.append(self.a)
        self.buttons.append(self.start)
        
    def update(self):
        for button in self.buttons:
            button.update()

    def update_event(self, event):
        for button in self.buttons:
            button.update_event(event)