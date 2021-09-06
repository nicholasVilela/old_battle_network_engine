from enum import Enum


class Scenes(Enum):
    BATTLE = 0
    SELECT = 1
    PAUSE  = 2
    END    = 3

class SceneStates(Enum):
    IDLE     = 0
    ACTIVE   = 1
    PAUSED   = 2
    FINISHED = 3

class Teams(Enum):
    RED  = 0
    BLUE = 1

class LivingStates(Enum):
    SPAWN     = 0
    IDLE      = 1
    MOVING    = 2
    ATTACKING = 3
    STAGGERED = 4

class TileStates(Enum):
    BASE   = 0
    CRACK  = 1
    BROKEN = 2

class ButtonStates(Enum):
    IDLE     = 0
    PRESSED  = 1
    HOLDING  = 2
    RELEASED = 3

class ChipStates(Enum):
    IDLE     = 0
    RUNNING  = 1
    FINISHED = 2

class LivingAnimations(Enum):
    SPAWN  = 0
    IDLE   = 1
    MOVING = 2
    ATTACK = 3

class PlayerAnimations(Enum):
    SPAWN        = 0
    IDLE         = 1
    MOVING       = 2
    ATTACK_SHOOT = 3
    ATTACK_SLASH = 4
    ATTACK_SWING = 5
    ATTACK_THROW = 6
    