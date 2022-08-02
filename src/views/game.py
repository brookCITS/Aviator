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
<<<<<<< HEAD
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
=======

>>>>>>> AVA-22


    def on_draw(self):


    def on_key_press(self, symbol,modifier):
        if symbol == arcade.key.RIGHT:
            print("Right arrow key is pressed")
            self.player.change_x = 4
        if symbol == arcade.key.LEFT:
            print("Left arrow key is pressed")
            self.player.change_x = -4
            
    def on_key_release(self, key, modifiers):
        if symbol == arcade.key.RIGHT:
            print("Right arrow key is pressed")
            self.player.change_x = 0
        if symbol == arcade.key.LEFT:
            print("Left arrow key is pressed")
            self.player.change_x = 0 

    def update(self, delta_time):
