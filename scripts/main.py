import pygame

from game import Game
from enums import Scenes
from config import WINDOW
from scenes import battle_scene, select_scene, pause_scene, end_scene
from resources import resources


pygame.init()
pygame.display.set_caption("Battle Network Engine")

screen = pygame.display.set_mode((WINDOW['width'], WINDOW['height']))

resources['scenes'] = {
    Scenes.BATTLE: battle_scene.BattleScene(Scenes.BATTLE),
    Scenes.SELECT: select_scene.SelectScene(Scenes.SELECT),
    Scenes.PAUSE: pause_scene.PauseScene(Scenes.PAUSE),
    Scenes.END: end_scene.EndScene(Scenes.END),
}

game = Game(screen, Scenes.BATTLE)
game.run()