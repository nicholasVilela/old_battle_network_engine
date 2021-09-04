from enums import LivingStates, TileStates


COLORS = {
    'black': (0, 0, 0),
    'dim_gray': (30, 30, 30),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (255, 0, 255),
    'cyan': (0, 255, 255),
}

SPRITES = {
    'tiles': {
        'red': {
            TileStates.BASE: '../assets/textures/tiles/tile_red.png'
        },
        'blue': {
            TileStates.BASE: '../assets/textures/tiles/tile_blue.png'
        }
    },
    'battlers': {
        'megaman': {
            LivingStates.IDLE: '../assets/textures/megaman/IDLE_spritesheet.png'
        },
    }
}

FONTS = {
    'base': '../assets/fonts/BN6FontBold.ttf'
}