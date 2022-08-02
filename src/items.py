import random
import arcade
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Cloud(arcade.Sprite):

    def __init__(self, filename, ,sprite_scaling, speed):
        super().__init__(filename, sprite_scaling)
        self.center_x = 0
        self.center_y = 0
        self.change_x = speed

    def update(self):
        self.center_x += self.change_x
