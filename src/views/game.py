import arcade
import time
import sys
sys.path.insert(0, 'src/views')

import gameover
from src.items import Plane, Cloud, MiniBossCloud, BossCloud

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGE_WIDTH = 882
SCROLL_SPEED = 2


class GameView(arcade.View):

    def __init__(self, options):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()
        self.options=options
        filename = "src/images/planes/"+self.options["color"]+".png"
        self.level = options['level']

        self.player=Plane(filename, 0.7)
        self.clouds=arcade.SpriteList()
        self.clouds_miniboss=arcade.SpriteList()

        self.clouds_boss=None
        self.birds=None
        self.background=None
        self.window.set_mouse_visible(False)
        self.score=0
        self.lives=3
        #set up based on levels
        if self.options["level"] == "beginner":
            speed = 3
            #5 regular clouds (speed slow)
            for cloud in range(5):
                self.clouds.append(Cloud("src/images/cloud.png",0.2, speed))
            #2 miniboss
            for cloud in range(2):
                self.clouds_miniboss.append(MiniBossCloud("src/images/boss.png",0.2, speed))
            self.clouds_boss = BossCloud("src/images/boss.png", 0.5, speed)

        elif self.options["level"] == "intermidiate":
            speed = 4
            #10 regular clouds (speed slow)
            for cloud in range(10):
                self.clouds.append(Cloud("src/images/cloud.png",0.2, speed))
            #2 miniboss
            for cloud in range(4):
                self.clouds_miniboss.append(MiniBossCloud("src/images/boss.png",0.2, speed))
            self.clouds_boss = BossCloud("src/images/boss.png", 0.5, speed)

        elif self.options["level"] == "advanced":
            speed = 5
            #15 regular clouds (speed slow)
            for cloud in range(15):
                self.clouds.append(Cloud("src/images/cloud.png",0.2, speed))
            #2 miniboss
            for cloud in range(6):
                self.clouds_miniboss.append(MiniBossCloud("src/images/boss.png",0.2, speed))
            self.clouds_boss = BossCloud("src/images/boss.png", 0.5, speed)

        #set up the background
        self.background_list = arcade.SpriteList()

        self.background_sprite = arcade.Sprite("src/images/background_night.png")

        self.background_sprite.center_x = IMAGE_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        self.background_sprite.change_x = -SCROLL_SPEED

        self.background_list.append(self.background_sprite)

        #second background image
        self.background_sprite_2 = arcade.Sprite("src/images/background_night.png")

        self.background_sprite_2.center_x = SCREEN_WIDTH + IMAGE_WIDTH // 2
        self.background_sprite_2.center_y = SCREEN_HEIGHT // 2
        self.background_sprite_2.change_x = -SCROLL_SPEED

        self.background_list.append(self.background_sprite_2)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.background_list.draw()
        self.player.draw()

    def on_key_press(self, symbol,modifier):
        if symbol == arcade.key.TOP:
            print("Right arrow key is pressed")
            self.player.change_x = 4
        if symbol == arcade.key.BOTTOM:
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
        #reset the images when they go past the screen
        for b in self.background_list:
            print("image width"+str(IMAGE_WIDTH))
            print("image left"+str(b.left))
            if b.left <= IMAGE_WIDTH*-1:
                b.center_x = SCREEN_WIDTH + IMAGE_WIDTH // 2
        self.background_list.update()

        #Check to see which round the player is in (clouds, miniboss, Boss)

            #normal clouds

            #miniboss

            #boss


        self.player.update()
