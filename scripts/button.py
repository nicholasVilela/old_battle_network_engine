import pygame
from enums import ButtonStates


class Button:
    def __init__(self, key):
        self.key = key
        self.state = ButtonStates.IDLE
        self.event = None

    def update(self):
        if self.state == ButtonStates.PRESSED or self.state == ButtonStates.RELEASED:
            self.state = ButtonStates.IDLE

        if self.event != None:
            if self.event.type == pygame.KEYDOWN and self.event.key == self.key and self.state == ButtonStates.IDLE:
                self.state = ButtonStates.PRESSED
            elif self.event.type == pygame.TEXTINPUT and pygame.key.key_code(self.event.text) == self.key and self.state == ButtonStates.IDLE:
                self.state = ButtonStates.PRESSED
            elif self.event.type == pygame.KEYUP and self.event.key == self.key and (self.state == ButtonStates.PRESSED or self.state == ButtonStates.HOLDING):
                self.state = ButtonStates.RELEASED
        elif pygame.key.get_pressed()[self.key]:
            print('ahh')
            self.state = ButtonStates.HOLDING
        
            self.event = None

    def update_event(self, event):
        self.event = event