from scenes import base_scene
from config import MAP, WINDOW, CONTROLLER
from const import COLORS, SPRITES
from entities.entity import Entity
from entities.living_entity import LivingEntity
from entities.player_entity import PlayerEntity
from entities.tile_entity import TileEntity
from entities.chip_entity import ChipEntity
from entities.spell_entity import SpellEntity
from instruction import Instruction
from sprite import Sprite, AnimatedSprite
from vec2 import Vec2
from util import map_to_world, tint_by_row, init_surface, is_red_team
from position import Position
from enums import LivingStates, Teams, TileStates, Stats, Chips, ChipStates, SpellTypes, SpellStates, Stats, PlayerAnimations
from animation import Animation
from resources import resources
from living_stat import Stat
import chips.cannon as cannon_chip
import chips.sword as sword_chip


class BattleScene(base_scene.BaseScene):
    def __init__(self, *args):
        super().__init__(*args)
        self.init_map()
        self.init_battlers()

    def render(self, screen):
        for key in self.layers:
            if key == 'battlers':
                for pos in self.layers[key]:
                    self.layers[key][pos].fill(COLORS['black'])
            else:
                self.layers[key].fill(COLORS['black'])

        for tile in resources['map']:
            tile.render()
                
        for key in self.entities:
            for entity in self.entities[key]:
                entity.render()

        for team in Teams:
            for entity in resources[team]:
                entity.render()

        for key in self.layers:
            if key == 'battlers':
                for pos in self.layers[key]:
                    screen.blit(self.layers[key][pos], (0, 0))
            else:
                screen.blit(self.layers[key], (0, 0))

    def update(self):
        super().update()
        for tile in resources['map']:
            tile.update()

        for team in Teams:
            for entity in resources[team]:
                entity.update()


    def init_entities(self):
        return {
            'chips' : [],
            'spells': [],
        }

    def init_layers(self):
        battler_layers = {}

        for y in range(MAP['height']):
            for x in range(MAP['width']):
                battler_layers[f'({x}, {y})'] = init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black'])

        return {
            'map'     : init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
            'red_battlers': init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
            'blue_battlers': init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
            'battlers': battler_layers,
            # 'battlers': init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
            'chips'   : init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
        }


    def init_map(self):
        for y in range(0, MAP['height']):
            for x in range(0, MAP['width']):
                scale = 2
                is_red = is_red_team(x)
                tint = tint_by_row(y, is_red, MAP['height'])

                tile = TileEntity(
                    name=f'tile_({x}, {y})',
                    sprite=Sprite(
                        path=SPRITES['tiles']['red' if is_red else 'blue'][TileStates.BASE],
                        layer=self.layers['map'],
                        size=Vec2(40, 30),
                        scale=scale,
                        tint=tint,
                    ),
                    position=Position(
                        _map=Vec2(x, y),
                        world=map_to_world(Vec2(x, y), scale)
                    ),
                    group=resources['map'],
                )

                self.spawn_entity(tile)

    def init_battlers(self):
        to_spawn = []

        megaman = PlayerEntity(
            name='Megaman',
            sprite=AnimatedSprite(
                path=SPRITES['battlers']['megaman'],
                layers=self.layers['battlers'],
                size=Vec2(64, 64),
                scale=2,
                entry_animation=PlayerAnimations.SPAWN,
                animations={
                    PlayerAnimations.SPAWN: Animation(
                        name=PlayerAnimations.SPAWN,
                        frame_count=18,
                        frame_duration=40,
                        loop=False,
                        playing=True,
                        instructions=[],
                    ),
                    PlayerAnimations.IDLE: Animation(
                        name=PlayerAnimations.IDLE,
                        frame_count=1,
                        frame_duration=0,
                        loop=True,
                        instructions=[],
                    ),
                    PlayerAnimations.MOVING: Animation(
                        name=PlayerAnimations.MOVING,
                        frame_count=5,
                        frame_duration=40,
                        loop=False,
                        instructions=[],
                    ),
                    PlayerAnimations.ATTACK_SHOOT: Animation(
                        name=PlayerAnimations.ATTACK_SHOOT,
                        frame_count=5,
                        frame_duration=50,
                        loop=False,
                        instructions=[],
                    ),
                    PlayerAnimations.ATTACK_SHOOT_HEAVY: Animation(
                        name=PlayerAnimations.ATTACK_SHOOT_HEAVY,
                        frame_count=13,
                        frame_duration=50,
                        loop=False,
                        instructions=[],
                    ),
                    PlayerAnimations.ATTACK_SLASH: Animation(
                        name=PlayerAnimations.ATTACK_SLASH,
                        frame_count=7,
                        frame_duration=500,
                        loop=False,
                        instructions=[],
                    ),
                },
            ),
            position=Position(
                _map=Vec2(1, 1),
                world=map_to_world(Vec2(1, 1), 2),
                offset=Vec2(-22, -90)
            ),
            group=resources[Teams.RED],
            team=Teams.RED,
            state=LivingStates.SPAWN,
            stats={
                Stats.HP: Stat(
                    _type=Stats.HP,
                    value=100
                ),
                Stats.MOVE_SPEED: Stat(
                    _type=Stats.MOVE_SPEED,
                    value=30
                )
            },
            chips=[
                # sword_chip.generate(self.entities['chips'], self.entities['spells'], self.layers['chips'], Teams.BLUE, Position(_map=Vec2(1, 1), world=map_to_world(Vec2(1, 1), 2))),
                # cannon_chip.generate(self.entities['chips'], self.entities['spells'], self.layers['chips'], Teams.BLUE, Position(_map=Vec2(1, 1), world=map_to_world(Vec2(1, 1), 2))),
            ]
        )

        mettaur = LivingEntity(
            name='Mettaur',
            sprite=AnimatedSprite(
                path=SPRITES['battlers']['mettaur'],
                layers=self.layers['battlers'],
                size=Vec2(64, 64),
                scale=2,
                animations={
                    LivingStates.IDLE: Animation(
                        name=LivingStates.IDLE,
                        frame_count=1,
                        frame_duration=0,
                        loop=True,
                        playing=True
                    )
                },
                entry_animation=LivingStates.IDLE
            ),
            position=Position(
                _map=Vec2(3, 1),
                world=map_to_world(Vec2(3, 1), 2),
                offset=Vec2(-25, -95)
            ),
            group=resources[Teams.BLUE],
            state=LivingStates.IDLE,
            team=Teams.BLUE,
            stats={
                Stats.HP: Stat(
                    _type=Stats.HP,
                    value=40,
                )
            },
        )

        to_spawn.append(megaman)
        to_spawn.append(mettaur)

        for entity in to_spawn:
            self.spawn_entity(entity)

    def spawn_entity(self, entity):
        entity.group.append(entity)