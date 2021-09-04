from enum import Enum


class Scenes(Enum):
    BATTLE = 0
    SELECT = 1
    PAUSE  = 2
    END    = 3

class SceneStates(Enum):
    QUIT     = 0
    IDLE     = 1
    RUNNING  = 2
    PAUSED   = 3
    FINISHED = 4