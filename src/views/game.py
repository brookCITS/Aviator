import arcade
import time
import sys
sys.path.insert(0, 'src/views')

import gameover

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameView(arcade.View):

    def __init__(self, options):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()



    def on_draw(self):
        pass

    def on_key_press(self, symbol,modifier):
        pass

    def on_key_release(self, key, modifiers):
        pass

    def update(self, delta_time):
        pass
