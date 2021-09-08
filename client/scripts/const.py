from enums import LivingStates, TileStates, Chips, PlayerAnimations, ChipStates


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
            PlayerAnimations.SPAWN: '../assets/textures/megaman/SPAWN_spritesheet.png',
            PlayerAnimations.IDLE: '../assets/textures/megaman/IDLE_spritesheet.png',
            PlayerAnimations.MOVING: '../assets/textures/megaman/MOVING_spritesheet.png',
            PlayerAnimations.ATTACK_SHOOT: '../assets/textures/megaman/ATTACK_SHOOT_spritesheet.png',
            PlayerAnimations.ATTACK_SHOOT_HEAVY: '../assets/textures/megaman/ATTACK_SHOOT_HEAVY_spritesheet.png',
        },
        'mettaur': {
            LivingStates.IDLE: '../assets/textures/enemies/mettaur/IDLE_spritesheet.png',
        },
    },
    'chips': {
        Chips.CANNON: {
            ChipStates.IDLE: '../assets/textures/chips/cannon/small_icon.png',
            ChipStates.RUNNING: '../assets/textures/chips/cannon/RUNNING_spritesheet.png',
        },
    },
}

FONTS = {
    'base': '../assets/fonts/BN6FontBold.ttf'
}