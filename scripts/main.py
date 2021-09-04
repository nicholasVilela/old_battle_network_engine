import pygame

from game import Game
from enums import Scenes
from config import WINDOW
from scenes import battle_scene, select_scene, pause_scene, end_scene


pygame.init()
pygame.display.set_caption("Battle Network Engine")

screen = pygame.display.set_mode((WINDOW['width'], WINDOW['height']))

scenes = {
    Scenes.BATTLE: battle_scene.BattleScene(),
    Scenes.SELECT: select_scene.SelectScene(),
    Scenes.PAUSE: pause_scene.PauseScene(),
    Scenes.END: end_scene.EndScene(),
}

game = Game(screen, scenes, Scenes.PAUSE)
game.run()