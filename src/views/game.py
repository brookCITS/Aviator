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


    def on_key_press(self, symbol,modifier):
         if symbol == arcade.key.RIGHT:
            print("Right arrow key is pressed")
            self.player.change_x = 0
      if symbol == arcade.key.LEFT:
            print("Left arrow key is pressed")
            self.player.change_x = 0 


    def on_key_release(self, key, modifiers):



    def update(self, delta_time):
