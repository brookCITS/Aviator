import arcade
import sys
import arcade.gui
sys.path.insert(0, 'src/views')
import game
import menu


class GameOverView(arcade.View):
    """ View to show when game is over """
    def __init__(self, options):
        """ This is run once when we switch to this view """
        super().__init__()
        self.options = options
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width - 1, 0, self.window.height - 1)
        self.window.set_mouse_visible(True)
    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.window.set_mouse_visible(True)
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()
        title_label = arcade.gui.UITextureButton(texture= arcade.load_texture('src/images/GAME OVER PIXEL.png'), scale=1)
        self.v_box.add(title_label.with_space_around(bottom=33))

        start_game_texture= arcade.load_texture('src/images/buttons/NewGame.png')
        start_game_texture_hovered= arcade.load_texture('src/images/buttons/NewGameClicked.png')

        NewGamebutton =  arcade.gui.UITextureButton(x=0, y=0, texture=start_game_texture, texture_hovered=start_game_texture_hovered, scale=0.4)
        self.v_box.add(NewGamebutton.with_space_around(bottom=33))

        start_game_texture= arcade.load_texture('src/images/buttons/Continue.png')
        start_game_texture_hovered= arcade.load_texture('src/images/buttons/ContinueClicked.png')

        Continuebutton = arcade.gui.UITextureButton(x=0, y=0, texture=start_game_texture, texture_hovered=start_game_texture_hovered, scale=0.4)
        self.v_box.add(Continuebutton.with_space_around(bottom=33))

        start_game_texture= arcade.load_texture('src/images/buttons/Exit.png')
        start_game_texture_hovered= arcade.load_texture('src/images/buttons/ExitClicked.png')

        Exitbutton = arcade.gui.UITextureButton(x=0, y=0, texture=start_game_texture, texture_hovered=start_game_texture_hovered, scale=0.4)
        self.v_box.add(Exitbutton.with_space_around(bottom=33))

        self.manager.add(arcade.gui.UIAnchorWidget(
                anchor_x='center_x',
                anchor_y='center_y',
                child=self.v_box)
        )

        @NewGamebutton.event("on_click")
        def on_click_flatbutton(event):
            print("New Game")

            game_view = menu.MenuView()
            self.window.show_view(game_view)

        @Continuebutton.event("on_click")
        def on_click_flatbutton(event):
            print("Continue")
            game_view = game.GameView(self.options)
            self.window.show_view(game_view)

        @Exitbutton.event("on_click")
        def on_click_flatbutton(event):
            print("Exit")
            arcade.exit()

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.manager.draw()
