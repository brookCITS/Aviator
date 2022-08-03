import random
import arcade
import time
from C import MenuView



#from src.views.menu import MenuView
# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Aviator")
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
