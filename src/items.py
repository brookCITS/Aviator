import random
import arcade
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 5


class Plane(arcade.Sprite):

 def __init__(self, filename, sprite_scaling):
  super().__init__(filename, sprite_scaling)
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


class Cloud(arcade.Sprite):

    def __init__(self, filename, sprite_scaling, speed):
        super().__init__(filename, sprite_scaling)
        self.center_x = SCREEN_WIDTH + self.right
        self.center_y = random.randint(99, SCREEN_HEIGHT)
        self.change_x = speed

    def update(self):
        self.center_x += self.change_x

class MiniBossCloud(Cloud):

    def __init__(self, filename, sprite_scaling, speed):
        super().__init__(filename, sprite_scaling, speed)
        self.center_x = self.right+SCREEN_WIDTH
        self.center_y = random.randint(99, SCREEN_HEIGHT)
        self.change_x = speed

class BossCloud(Cloud):

    def __init__(self, filename, sprite_scaling, speed):
        super().__init__(filename, sprite_scaling, speed)
        self.center_x = self.right+SCREEN_WIDTH
        self.center_y = random.randint(99, SCREEN_HEIGHT)
        self.change_x = speed

    def update_x(self):
        if self.center_x >= 750:
            self.center_x += self.change_x

    def update_y(self, user_y):
        self.center_y = user_y

class Bird(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.cur_texture = 0
        self.center_x = 99+SCREEN_WIDTH
        self.center_y = random.randint(99, SCREEN_HEIGHT)
        self.textures = [
            arcade.load_texture("src/images/bird1.png"),
            arcade.load_texture("src/images/bird2.png")
        ]
        self.scale = 0.2

    def update(self):
        self.center_x -= 4

    def update_animation( self, delta_time: float = 1 / 60):
        self.cur_texture += 1
        if self.cur_texture > 1 * UPDATES_PER_FRAME:
            self.cur_texture = 0
            self.scale = 0.17
        frame = self.cur_texture // UPDATES_PER_FRAME

        self.texture = self.textures[frame]
class Lightining(arcade.Sprite):
    def __init__(self):
        filename = "src/images/lighting.png"
        sprite_scaling = 0.3
        super().__init__(filename, sprite_scaling)
        self.center_x = SCREEN_WIDTH + self.right
        self.change_x = 2

    def update_l(self):
        self.center_y = center_y
        self.center_x += self.change_x
