import arcade

# Creating MainGame class
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(700, 600, title = "../images/Night.png")

        # Loading the background image
        self.background = arcade.load_texture("../images/Night.png")

    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()

        # Drawing the background image
        arcade.draw_texture_rectangle(350, 300, 700,
                                      600, self.background)

# Calling MainGame class
MainGame()
arcade.run()
