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
        filename = "src/images/"+self.options["color"]+".png"
      self.player=Plane(filename, 0.3)
      self.clouds = arcade.SpriteList()
      self.clouds_miniboss = arcade.SpriteList()

      if self.option["level"] == "beginner":
        speed = 3
        #5 regular clouds (speed slow)
        for cloud in range(5):
          self.clouds.append(Cloud("src/images/cloud.png",0.2, speed))
          #2 miniboss 
        for cloud in range(2):
            self.clouds_miniboss.append(MiniBossCloud("src/images/miniboss.png",0.2, speed))
          
          self.clouds_boss = BossCloud("src/images/miniboss.png", 0.5, speed)
          
        
      elif self.option["level"] == "intermidiate":
        speed = 4
        #10 regular clouds (speed slow)
        for cloud in range(10):
          self.clouds.append(Cloud("src/images/cloud.png",0.2, speed))
          #2 miniboss 
        for cloud in range(4):
            self.clouds_miniboss.append(MiniBossCloud("src/images/miniboss.png",0.2, speed))
        self.clouds_boss = BossCloud("src/images/miniboss.png", 0.5, speed)
        
      elif self.option["level"] == "advanced":
        speed = 5
        #15 regular clouds (speed slow)
        for cloud in range(15):
          self.clouds.append(Cloud("src/images/cloud.png",0.2, speed))
          #2 miniboss 
        for cloud in range(6):
            self.clouds_miniboss.append(MiniBossCloud("src/images/miniboss.png",0.2, speed))
          
        self.clouds_boss = BossCloud("src/images/miniboss.png", 0.5, speed)

    def on_key_press(self, symbol,modifier):


    def on_key_release(self, key, modifiers):



    def update(self, delta_time):
