import arcade
import sys
import arcade.gui
import views
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
        title_label = arcade.gui.UITextArea(text="GameOver",font_size=30,font_name="New Times Roman")
        title_label.fit_content()
        self.v_box.add(title_label)

        NewGamebutton = arcade.gui.UIFlatButton(text="New Game", width=123, height=44)
        self.v_box.add(NewGamebutton.with_space_around(bottom=33))

        Continuebutton = arcade.gui.UIFlatButton(text="Continue", width=123, height=44)
        self.v_box.add(Continuebutton.with_space_around(bottom=33))

        Exitbutton = arcade.gui.UIFlatButton(text="Exit", width=123, height=44)
        self.v_box.add(Exitbutton.with_space_around(bottom=33))

        self.manager.add(arcade.gui.UIAnchorWidget(
                anchor_x='center_x',
                anchor_y='center_y',
                child=self.v_box)
        )

        @NewGamebutton.event("on_click")
        def on_click_flatbutton(event):
            print("New Game")
            game_view = MenuView(self.options)
            self.window.show_view(game_view)

        @Continuebutton.event("on_click")
        def on_click_flatbutton(event):
            print("Continue")
            game_view = GameView(self.options)
            self.window.show_view(game_view)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.manager.draw()
