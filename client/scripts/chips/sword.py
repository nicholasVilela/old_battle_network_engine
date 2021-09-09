from entities.chip_entity import ChipEntity
from entities.spell_entity import SpellEntity
from sprite import AnimatedSprite
from vec2 import Vec2
from const import SPRITES
from animation import Animation
from position import Position
from enums import Chips, ChipStates, SpellStates, SpellTypes, Stats, PlayerAnimations


def generate(chip_group, spell_group, layers, enemy_team, entry_position):
    return ChipEntity(
        name=Chips.SWORD,
        sprite=AnimatedSprite(
            path=SPRITES['chips'][Chips.SWORD],
            layers=layers,
            size=Vec2(64, 80),
            scale=2,
            animations={
                ChipStates.IDLE: Animation(
                    name=ChipStates.IDLE,
                    frame_count=1,
                    frame_duration=0,
                    offset=Vec2(-20, 0)
                ),
                ChipStates.RUNNING: Animation(
                    name=ChipStates.RUNNING,
                    frame_count=6,
                    frame_duration=500,
                ),
            },
            entry_animation=ChipStates.IDLE,
        ),
        position=Position(
            _map=Vec2(entry_position.map.x, entry_position.map.y),
            world=Vec2(entry_position.world.x, entry_position.world.y),
            offset=Vec2(-30, -100),
        ),
        group=chip_group,
        animation_type=PlayerAnimations.ATTACK_SLASH,
        spells=[
            SpellEntity(
                name=Chips.SWORD,
                sprite=None,
                position=Position(),
                group=spell_group,
                state=SpellStates.IDLE,
                _type=SpellTypes.HITSCAN,
                modifier=-80,
                stat=Stats.HP,
                affected=[Vec2(1,0)],
                enemy_team=enemy_team,
            ),
        ]
    )