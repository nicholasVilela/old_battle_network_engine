from scenes import base_scene
from config import MAP, WINDOW
from const import COLORS, SPRITES
from entities.entity import Entity
from sprite import Sprite
from vec2 import Vec2
from util import map_to_screen, tint_by_row, init_surface, is_red_team
from position import Position


class BattleScene(base_scene.BaseScene):
    def __init__(self, *args):
        super().__init__(*args)
        self.init_map()

    def update(self):
        pass

    def get_event(self, event):
        pass

    def init_entities(self):
        return {
            'map'     : [],
            'battlers': [],
        }

    def init_layers(self):
        return {
            'map'     : init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
            'battlers': init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
        }


    def init_map(self):
        self.entities['map'] = []

        for y in range(0, MAP['height']):
            for x in range(0, MAP['width']):
                scale = 2
                is_red = is_red_team(x)
                tint = tint_by_row(y, is_red, MAP['height'])

                tile = Entity(
                    name=f'tile_({x}, {y})',
                    sprite=Sprite(
                        path=SPRITES['tiles']['red' if is_red else 'blue']['default'],
                        layer=self.layers['map'],
                        size=Vec2(40, 30),
                        scale=scale,
                        tint=tint,
                    ),
                    position=Position(
                        _map=Vec2(x, y),
                        world=map_to_screen(x, y, scale)
                    ),
                    group=self.entities['map'],
                )

                self.spawn_entity(tile)

    def spawn_entity(self, entity):
        entity.group.append(entity)