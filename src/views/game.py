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
        self.options=options

        self.player=None
        self.clouds=None
        self.clouds_miniboss=None
        self.clouds_boss=None
        self.birds=None
        self.background=None
        self.set_mouse_visible(False)
        self.score=0
        self.lives=3


    def on_draw(self):


    def on_key_press(self, symbol,modifier):


    def on_key_release(self, key, modifiers):



    def update(self, delta_time):
