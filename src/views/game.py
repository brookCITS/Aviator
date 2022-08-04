import arcade
import time
import sys
sys.path.insert(0, 'src/views')

import gameover
from src.items import Plane, Cloud, MiniBossCloud, BossCloud, Bird, Lightining

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGE_WIDTH = 882
SCROLL_SPEED = 2


class GameView(arcade.View):

    def __init__(self, options):
        self.options = options
        print(options)
        """ Initializer """
        # Call the parent class initializer
        super().__init__()
        filename = "src/images/planes/"+self.options['color']+".png"

        self.player=Plane(filename, 2.1)
        self.player.center_x = 111
        self.player.center_y = 233
        self.clouds=arcade.SpriteList()
        self.clouds_miniboss=arcade.SpriteList()
        self.Lightining_sprites = arcade.SpriteList()
        self.wave = 1
        self.clouds_boss=None
        self.birds=None
        self.background=None
        self.window.set_mouse_visible(False)
        self.score=0
        self.lives=3
        #set up based on levels
        if self.options["level"] == "beginner":
            count = 1
            speed = -6
            #5 regular clouds (speed slow)
            for cloud in range(5):
                cloud = Cloud("src/images/cloud.png",0.5, speed)
                self.clouds.append(cloud)
                cloud.center_x *= count
                count+=1
                print(cloud.center_x)
                print(cloud.center_y)
            #2 miniboss
            count = 1
            for cloud in range(2):
                cloud = MiniBossCloud("src/images/boss.png",0.5, speed)
                self.clouds_miniboss.append(cloud)
                cloud.center_x += count
                print(cloud.center_x)
                count+=600
            self.clouds_boss = BossCloud("src/images/boss.png", 0.6, speed)

        elif self.options["level"] == "intermediate":
            speed = -7
            count = 1
            #10 regular clouds (speed slow)
            for cloud in range(10):
                cloud = Cloud("src/images/cloud.png",0.5, speed)
                cloud.center_x *= count
                count+=1
                self.clouds.append(cloud)

            count = 1
            #2 miniboss
            for cloud in range(4):
                cloud = MiniBossCloud("src/images/boss.png",0.5, speed)
                cloud.center_x += count
                count+=600
                self.clouds_miniboss.append(cloud)

            self.clouds_boss = BossCloud("src/images/boss.png", 0.6, speed)
            print(self.clouds_boss)

        elif self.options["level"] == "expert":
            print("expert level")
            speed = -8
            count = 1
            #15 regular clouds (speed slow)
            for cloud in range(15):
                cloud = Cloud("src/images/cloud.png",0.5, speed)
                cloud.center_x += count
                count+=600
                self.clouds.append(cloud)
            #2 miniboss
            count = 1
            for cloud in range(6):
                cloud = MiniBossCloud("src/images/boss.png",0.5, speed)
                cloud.center_x += count
                print(cloud.center_x)
                count+=600
                self.clouds_miniboss.append(cloud)
            self.clouds_boss = BossCloud("src/images/boss.png", 0.6, speed)

        #add birds
        self.bird_sprites = arcade.SpriteList()
        count = 1
        for bird in range(10):
            bird = Bird()
            bird.center_x += count
            count+=350
            self.bird_sprites.append(bird)

        count = 1
        for l in range(10):
            l = Lightining()
            l.center_x += count
            count+=350
            self.Lightining_sprites.append(l)

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
        self.clouds.draw()

        self.clouds_miniboss.draw()
        self.clouds_boss.draw()
        self.bird_sprites.draw()
        self.Lightining_sprites.draw()

        self.player.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output = f"Level: {self.options['level']}"
        arcade.draw_text(output, 200, 20, arcade.color.WHITE, 14)

        output = f"Lives: {self.lives}"
        arcade.draw_text(output, 400, 20, arcade.color.WHITE, 14)

    def on_key_press(self, symbol,modifier):
        if symbol == arcade.key.UP:
            print("top arrow key is pressed")
            self.player.change_y = 4
        if symbol == arcade.key.DOWN:
            print("bottom arrow key is pressed")
            self.player.change_y = -4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            print("top arrow key is pressed")
            self.player.change_y = 0
        if key == arcade.key.DOWN:
            print("bottom arrow key is pressed")
            self.player.change_y = 0




    def update(self, delta_time):
        #check if we need to end the game
        if self.lives <= 0:
            endgame = gameover.GameOverView(self.options)
            self.window.show_view(endgame)

        #reset the images when they go past the screen
        for b in self.background_list:
            #print("image width"+str(IMAGE_WIDTH))
            #print("image left"+str(b.left))
            if b.left <= IMAGE_WIDTH*-1:
                b.center_x = SCREEN_WIDTH + IMAGE_WIDTH // 2
        self.background_list.update()

        #Check to see which round the player is in (clouds, miniboss, Boss)
        if self.wave ==1:
            #normal clouds
            collide = arcade.check_for_collision_with_list(self.player, self.clouds)
            for cloud in collide:
                self.lives -= 1
                cloud.remove_from_sprite_lists()

            for cloud in self.clouds:
                if cloud.right < 0:
                    self.score += 1
                    self.clouds.pop(self.clouds.index(cloud))
            if len(self.clouds) == 0:
                self.wave = 2
            self.clouds.update()

        elif self.wave == 2:
            #miniboss
            collide = arcade.check_for_collision_with_list(self.player, self.clouds_miniboss)
            for cloud in collide:
                self.lives -= 1
                cloud.remove_from_sprite_lists()

            for cloud in self.clouds_miniboss:
                print(cloud.center_x)
                if cloud.right < 0:
                    self.score += 1
                    self.clouds_miniboss.pop(self.clouds_miniboss.index(cloud))

            if len(self.clouds_miniboss) == 0:
                self.wave = 3
            self.clouds_miniboss.update()
        else:
            collide = arcade.check_for_collision(self.player, self.clouds_boss)
            if collide:
                self.lives -= 1
                print("game over")
            self.clouds_boss.update_x()
            self.clouds_boss.update_y(self.player.center_y)

            #for l in self.Lightining_sprites:
                #l.update_l(self.player.center_y)
            #boss

        self.bird_sprites.update_animation()
        self.bird_sprites.update()
        self.player.update()
