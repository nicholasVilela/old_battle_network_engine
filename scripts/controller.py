import pygame

from copy import copy
from button import Button
from enums import Buttons
from publisher import Publisher


class Controller(Publisher):
    def __init__(self, broker, up, down, left, right, b, a, start):
        super().__init__(broker)
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.b = b
        self.a = a
        self.start = start

        self.buttons = self.load_buttons()

    def load_buttons(self):
        return {
            Buttons.UP   : Button(Buttons.UP, getattr(pygame, self.up)),
            Buttons.DOWN : Button(Buttons.DOWN, getattr(pygame, self.down)),
            Buttons.LEFT : Button(Buttons.LEFT, getattr(pygame, self.left)),
            Buttons.RIGHT: Button(Buttons.RIGHT ,getattr(pygame, self.right)),
            Buttons.A    : Button(Buttons.A ,getattr(pygame, self.a)),
            Buttons.B    : Button(Buttons.B ,getattr(pygame, self.b)),
            Buttons.START: Button(Buttons.START ,getattr(pygame, self.start))
        }
        
    def update(self):
        for key in self.buttons:
            self.buttons[key].update(self.publish)

    def get_event(self, event):
        for key in self.buttons:
            self.buttons[key].get_event(event)