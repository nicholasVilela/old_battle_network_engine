from scenes import base_scene
from config import MAP, WINDOW, CONTROLLER
from const import COLORS, SPRITES
from entities.entity import Entity
from entities.living_entity import LivingEntity
from entities.player_entity import PlayerEntity
from entities.chip_entity import ChipEntity
from entities.spell_entity import SpellEntity
from sprite import Sprite, AnimatedSprite
from vec2 import Vec2
from util import map_to_world, tint_by_row, init_surface, is_red_team
from position import Position
from enums import LivingStates, Teams, TileStates, Stats, Chips, ChipStates, SpellTypes, SpellStates, Stats, PlayerAnimations
from animation import Animation
from resources import resources
from living_stat import Stat


class BattleScene(base_scene.BaseScene):
    def __init__(self, *args):
        super().__init__(*args)
        self.init_map()
        self.init_battlers()

    def render(self):
        for key in self.layers:
            self.layers[key].fill(COLORS['black'])
        for key in self.entities:
            for entity in self.entities[key]:
                entity.render()

        for team in Teams:
            for entity in resources[team]:
                entity.render()

    def update(self):
        super().update()
        for team in Teams:
            for entity in resources[team]:
                entity.update()

    def init_entities(self):
        return {
            'map'   : [],
            'chips' : [],
            'spells': [],
        }

    def init_layers(self):
        return {
            'map'     : init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
            'battlers': init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
            'chips': init_surface(Vec2(WINDOW['width'], WINDOW['height']), COLORS['black']),
        }


    def init_map(self):
        for y in range(0, MAP['height']):
            for x in range(0, MAP['width']):
                scale = 2
                is_red = is_red_team(x)
                tint = tint_by_row(y, is_red, MAP['height'])

                tile = Entity(
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
                    group=self.entities['map'],
                )

                self.spawn_entity(tile)

    def init_battlers(self):
        to_spawn = []

        megaman = PlayerEntity(
            name='Megaman',
            sprite=AnimatedSprite(
                path=SPRITES['battlers']['megaman'],
                layer=self.layers['battlers'],
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
                    ),
                    PlayerAnimations.IDLE: Animation(
                        name=PlayerAnimations.IDLE,
                        frame_count=1,
                        frame_duration=0,
                        loop=True,
                    ),
                    PlayerAnimations.MOVING: Animation(
                        name=PlayerAnimations.MOVING,
                        frame_count=5,
                        frame_duration=40,
                        loop=False,
                    ),
                    PlayerAnimations.ATTACK_SHOOT: Animation(
                        name=PlayerAnimations.ATTACK_SHOOT,
                        frame_count=5,
                        frame_duration=85,
                        loop=False,
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
                ChipEntity(
                    name=Chips.CANNON,
                    sprite=AnimatedSprite(
                        path=SPRITES['chips'][Chips.CANNON],
                        layer=self.layers['chips'],
                        size=Vec2(64, 64),
                        scale=2,
                        animations={
                            ChipStates.RUNNING: Animation(
                                name=ChipStates.RUNNING,
                                frame_count=9,
                                frame_duration=50,
                            ), 
                        },
                        entry_animation=ChipStates.RUNNING,
                    ),
                    position=Position(
                        _map=Vec2(0, 0),
                        world=Vec2(0, 0),
                        offset=Vec2(60, -90),
                    ),
                    group=self.entities['chips'],
                    spells=[
                        SpellEntity(
                            name=Chips.CANNON,
                            sprite=None,
                            position=Position(),
                            group=self.entities['spells'],
                            state=SpellStates.IDLE,
                            _type=SpellTypes.HITSCAN,
                            modifier=-40,
                            stat=Stats.HP,
                            affected=[Vec2(1,0), Vec2(2,0), Vec2(3,0), Vec2(4,0), Vec2(5,0)],
                            team=Teams.BLUE,
                        ),
                    ]
                )
            ]
        )

        mettaur = LivingEntity(
            name='Mettaur',
            sprite=AnimatedSprite(
                path=SPRITES['battlers']['mettaur'],
                layer=self.layers['battlers'],
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
                _map=Vec2(4, 1),
                world=map_to_world(Vec2(4, 1), 2),
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