import pygame
from enums import ButtonStates, PublisherDataTypes
from publisher import PublisherData


class Button:
    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.state = ButtonStates.IDLE
        self.event = None

    def update(self, callback):
        if self.state == ButtonStates.PRESSED or self.state == ButtonStates.RELEASED:
            self.state = ButtonStates.IDLE

        if self.event != None:
            if self.event.type == pygame.KEYDOWN and self.event.key == self.key and self.state == ButtonStates.IDLE:
                self.state = ButtonStates.PRESSED
                callback(PublisherData({'button': self.name, 'state': self.state}, PublisherDataTypes.CONTROLLER))
            elif self.event.type == pygame.TEXTINPUT and pygame.key.key_code(self.event.text) == self.key and self.state == ButtonStates.IDLE:
                self.state = ButtonStates.PRESSED
                callback(PublisherData({'button': self.name, 'state': self.state}, PublisherDataTypes.CONTROLLER))
            elif self.event.type == pygame.KEYUP and self.event.key == self.key and (self.state == ButtonStates.PRESSED or self.state == ButtonStates.HOLDING):
                self.state = ButtonStates.RELEASED
                callback(PublisherData({'button': self.name, 'state': self.state}, PublisherDataTypes.CONTROLLER))
        elif pygame.key.get_pressed()[self.key]:
            self.state = ButtonStates.HOLDING
            callback(PublisherData({'button': self.name, 'state': self.state}, PublisherDataTypes.CONTROLLER))

        self.event = None

    def get_event(self, event):
        self.event = event