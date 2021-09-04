import pygame

from resources import resources
from enums import SceneStates
from config import TILE, MAP
from vec2 import Vec2
from rgb import RGB
from enums import Teams


def map_to_world(position, scale=1):
    offset_x = 0
    offset_y = 250

    screen_x = offset_x + (TILE['surface_width'] * position.x * scale)
    screen_y = offset_y + (TILE['surface_height'] * position.y * scale)

    return Vec2(screen_x, screen_y)

def init_surface(screen_size, colorkey):
    surface = pygame.Surface((screen_size.x, screen_size.y))
    surface.set_colorkey(colorkey)

    return surface

def check_position(position, team):
    if position.y >= 0 and position.y < MAP['height']:
        if team == Teams.RED:
            return position.x >= 0 and position.x < (MAP['width'] / 2)
        else:
            return False

    return False

def is_red_team(x):
    return x >= 0 and x < (MAP['width'] / 2)

def tint_by_row(row, is_red, row_limit):
    lightest = RGB(255, 255, 255)
    darkest = RGB(210, 160, 110) if is_red else RGB(110, 160, 210)

    if row < 0 or row >= row_limit or row_limit <= 0:
        return
    elif row == 0:
        return darkest
    elif row == row_limit - 1:
        return lightest
    else:
        delta = lightest - darkest
        step = delta / row_limit
        product = step * row

        color = darkest + product

        return color

def push_scene(target_scene):
    active_scene = resources['scene_stack'][-1]
    active_scene.state = SceneStates.IDLE

    resources['scene_stack'].append(resources['scenes'][target_scene])

    active_scene = resources['scene_stack'][-1]
    active_scene.state = SceneStates.ACTIVE