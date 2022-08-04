import random
import arcade
import time
import gameover
from gameover import GameOverView

#from src.views.menu import MenuView
# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Aviator")
    start_view = GameOverView({"Color": "green"})
    window.show_view(start_view)
    arcade.run()



if __name__ == "__main__":
    main()
