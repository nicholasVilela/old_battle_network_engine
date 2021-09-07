from entities.chip_entity import ChipEntity
from entities.spell_entity import SpellEntity
from sprite import AnimatedSprite
from vec2 import Vec2
from const import SPRITES
from animation import Animation
from position import Position
from enums import Chips, ChipStates, SpellStates, SpellTypes, Stats


def generate(chip_group, spell_group, chip_layer, enemy_team):
    return ChipEntity(
        name=Chips.CANNON,
        sprite=AnimatedSprite(
            path=SPRITES['chips'][Chips.CANNON],
            layer=chip_layer,
            size=Vec2(64, 64),
            scale=2,
            animations={
                ChipStates.IDLE: Animation(
                    name=ChipStates.IDLE,
                    frame_count=1,
                    frame_duration=0,
                ),
                ChipStates.RUNNING: Animation(
                    name=ChipStates.RUNNING,
                    frame_count=9,
                    frame_duration=50,
                ),
            },
            entry_animation=ChipStates.IDLE,
        ),
        position=Position(
            _map=Vec2(0, 0),
            world=Vec2(0, 0),
            offset=Vec2(54, -90),
        ),
        group=chip_group,
        spells=[
            SpellEntity(
                name=Chips.CANNON,
                sprite=None,
                position=Position(),
                group=spell_group,
                state=SpellStates.IDLE,
                _type=SpellTypes.HITSCAN,
                modifier=-40,
                stat=Stats.HP,
                affected=[Vec2(1,0), Vec2(2,0), Vec2(3,0), Vec2(4,0), Vec2(5,0)],
                enemy_team=enemy_team,
            ),
        ]
    )