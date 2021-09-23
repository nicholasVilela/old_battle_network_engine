import pygame


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

class PanelConfig:
    def __init__(self, size: Rectangle, surface_size: Rectangle):
        self.size = size
        self.surface_size = surface_size

class GameConfig:
    def __init__(self, grid: Rectangle, panel: PanelConfig):
        self.grid = grid
        self.panel = panel

class Config:
    def __init__(self, title: str, window: Rectangle, scale: float, fps: int, game: GameConfig):
        self.title = title
        self.window = window
        self.scale = scale
        self.fps = fps

        self.game = game