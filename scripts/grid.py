from resources import resources
from const import SPRITES

from entities.entity import Entity

from components.position_component import PositionComponent
from components.sprite_component import SpriteComponent

from enums import ComponentTypes


class Grid:
    def __init__(self, group):
        self.panels = self.create_grid(group)

    def create_grid(self, group):
        grid_height = resources['config'].game.grid.height
        grid_width = resources['config'].game.grid.width

        for y in range(0, grid_height):
            for x in range(0, grid_width):
                panel = Entity(
                    name=f'panel_({x}, {y})',
                    components=[
                        PositionComponent(),
                        SpriteComponent(path=SPRITES['tiles']['red']),
                    ],
                    group=group,
                )

                panel.set_parent(panel)

                

        # for y in range(0, resources['config'].game.grid.height):
        #     for x in range(0, resources['config'].game.grid.width):
        #         scale = 2
        #         is_red = is_red_team(x)
        #         tint = tint_by_row(y, is_red, resources['config'].game.grid.height)

        #         tile = TileEntity(
        #             name=f'tile_({x}, {y})',
        #             sprite=Sprite(
        #                 path=SPRITES['tiles']['red' if is_red else 'blue'][TileStates.BASE],
        #                 layer=self.layers['map'],
        #                 size=Vec2(40, 30),
        #                 scale=scale,
        #                 tint=tint,
        #             ),
        #             position=Position(
        #                 _map=Vec2(x, y),
        #                 world=map_to_world(Vec2(x, y), scale)
        #             ),
        #             group=resources['map'],
        #         )

        #         self.spawn_entity(tile)