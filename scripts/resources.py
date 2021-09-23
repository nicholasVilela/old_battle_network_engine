from enums import Teams
from broker import Broker
import yaml

from config import Config, GameConfig, PanelConfig, Rectangle


def load_config():
    config_path = '../config/config.yaml'
    game_path = '../config/game.yaml'

    with open(game_path) as file:
        game_data = yaml.load(file, Loader=yaml.FullLoader)

        game_config = GameConfig(
            grid=Rectangle(
                width=game_data['grid']['width'],
                height=game_data['grid']['height'],
            ),
            panel=PanelConfig(
                size=Rectangle(
                    width=game_data['panel']['size']['width'],
                    height=game_data['panel']['size']['height'],
                ),
                surface_size=Rectangle(
                    width=game_data['panel']['surface_size']['width'],
                    height=game_data['panel']['surface_size']['height'],
                )
            )
        )

    with open(config_path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

        config = Config(
            title=data['title'],
            window=Rectangle(
                width=data['window']['width'],
                height=data['window']['height'],
            ),
            scale=data['scale'],
            fps=data['fps'],
            game=game_config,
        )

    return config

resources = {
    'config': load_config(),
    'scenes': {},
    'scene_stack': [],
    'dt': 0,
    'map': [],
    'broker': Broker(),
    Teams.RED : [],
    Teams.BLUE: [],
}