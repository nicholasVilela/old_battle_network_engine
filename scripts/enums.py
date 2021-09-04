from enum import Enum


class Scenes(Enum):
    BATTLE = 0
    SELECT = 1
    PAUSE  = 2
    END    = 3

class SceneStates(Enum):
    IDLE     = 0
    RUNNING  = 1
    PAUSED   = 2
    FINISHED = 3

class Teams(Enum):
    RED  = 0
    BLUE = 1