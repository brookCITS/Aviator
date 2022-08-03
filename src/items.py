import random
import arcade
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Plane(arcade.Sprite):

 def __init__(self, filename, sprite_scaling):
  super()._init_(filename, sprite.scaling)
  self.change_x = 0
  self.change_y = 0
  self.center_y = 75
  self.center_x = 300

 def restart(self):
  self.center_x = 300
  self.center_y = 75

 def update(self):
  self.center_x += self.change_x
  self.center_y += self.change_y
  
 if self.center._x > SCREEN_WIDTH - self.width / 2:
    self.change_x *= -1
 if self.center_y > SCREEN_WIDTH - self.width / 2:
    self.change_y *= -1
   
 if self.center_x < SCREEN_WIDTH - self.width / 2:
   self.change_x *= -1
 if self.center_y < SCREEN_WIDTH - self.width / 2:
   self.change_y *= -1


class Cloud(arcade.Sprite):

    def __init__(self, filename, ,sprite_scaling, speed):
        super().__init__(filename, sprite_scaling)
        self.center_x = 0
        self.center_y = 0
        self.change_x = speed

    def update(self):
        self.center_x += self.change_x

class MiniBossCloud(Cloud):

    def __init__(self, filename, sprite_scaling, speed):
        super().__init__(filename, sprite_scaling, speed)
        self.center_x = 0
        self.center_y = 0
        self.change_x = speed

class BossCloud(Cloud):

    def __init__(self, filename, sprite_scaling, speed):
        super().__init__(filename, sprite_scaling, speed)
        self.center_x = 0
        self.center_y = 0
        self.change_x = speed
