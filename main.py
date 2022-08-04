import random
import arcade
import time
from src.views import MenuView

from pyglet.image import load as pyglet_load


# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Aviator")
    window.set_icon(pyglet_load("src/green_clicked.ico"))
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
