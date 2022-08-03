import arcade
import arcade.gui
import sys
sys.path.insert(0, 'src/views')
#import views
import game



class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.options = {
            'color': 'green',
            'level': 'beginner'
            }
        self.background = None

    def on_show_view(self):
        self.background = arcade.load_texture("src/images/Nighttime background.png")
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

        self.window.set_mouse_visible(True)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()

        self.h_box = arcade.gui.UIBoxLayout()
        self.h_box.vertical = False

        self.h_box2 = arcade.gui.UIBoxLayout()
        self.h_box2.vertical = False

        self.h_box3 = arcade.gui.UIBoxLayout()
        self.h_box3.vertical = False

#DISPLAY
#------------------
    #GAME TITLE
        title_label = arcade.gui.UITextureButton(texture=arcade.load_texture("src/images/AVIATOR LOGO.png"))

    #COLOR CHOOSE
        color_choose_text = arcade.gui.UITextureButton(texture=arcade.load_texture("src/images/chosen/color.png"))

    #COLORS
        green = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('src/images/planes/green.png'), texture_hovered=arcade.load_texture('src/images/planes/green_clicked.png'), scale=2)
        blue = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('src/images/planes/blue.png'), texture_hovered=arcade.load_texture('src/images/planes/blue_clicked.png'), scale=2)
        white = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('src/images/planes/white.png'), texture_hovered=arcade.load_texture('src/images/planes/white_clicked.png'), scale=2)
        yellow = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('src/images/planes/yellow.png'), texture_hovered=arcade.load_texture('src/images/planes/yellow_clicked.png'), scale=2)

    #LEVEL CHOOSE
        level_choose_text = arcade.gui.UITextureButton(texture=arcade.load_texture("src/images/chosen/difficulty.png"))
        level_beginner = arcade.gui.UITextureButton(texture=arcade.load_texture('src/images/buttons/beginner.png'), texture_hovered=arcade.load_texture('src/images/buttons/beginner_clicked.png'), scale=.8)
        level_intermediate = arcade.gui.UITextureButton(texture=arcade.load_texture('src/images/buttons/intermediate.png'), texture_hovered=arcade.load_texture('src/images/buttons/intermediate_clicked.png'), scale=.8)
        level_expert = arcade.gui.UITextureButton(texture=arcade.load_texture('src/images/buttons/expert.png'), texture_hovered=arcade.load_texture('src/images/buttons/expert_clicked.png'), scale=.8)

    #FINAL CHOICE
        color_choice = arcade.gui.UITextureButton(texture=arcade.load_texture("src/images/chosen/green_choice.png"))
        level_choice = arcade.gui.UITextureButton(texture=arcade.load_texture("src/images/chosen/beginner_choice.png"))

    #START
        start_game = arcade.gui.UITextureButton(texture= arcade.load_texture('src/images/buttons/start_g.png'), texture_hovered=arcade.load_texture('src/images/buttons/start_green_clicked.png'), scale=.7)

#CODE THAT ADDS TO DISPLAY
#-------------------------
#GAME TITLE
        self.v_box.add(title_label.with_border(width=0, color=arcade.color.BLACK).with_space_around(bottom=0))

#COLOR CHOOSE
        self.v_box.add(color_choose_text.with_space_around(bottom=0))
    #COLORS
        self.h_box.add(green.with_space_around(right=10))
        self.h_box.add(blue.with_space_around(right=10))
        self.h_box.add(white.with_space_around(right=10))
        self.h_box.add(yellow)
        self.v_box.add(self.h_box.with_space_around(bottom=0))

#LEVEL CHOOSE
        self.v_box.add(level_choose_text.with_space_around(bottom=0, top=0))
    #LEVELS
        self.h_box2.add(level_beginner.with_space_around(right=10))
        self.h_box2.add(level_intermediate.with_space_around(right=10))
        self.h_box2.add(level_expert)
        self.v_box.add(self.h_box2.with_space_around(bottom=0))

#CHOICES
        self.h_box3.add(color_choice.with_space_around(right=20))
        self.h_box3.add(level_choice)
        self.v_box.add(self.h_box3.with_space_around(bottom=0))

#START BUTTON
        self.v_box.add(start_game.with_space_around(top=0))

#DISPLAY ALL
        self.manager.add(arcade.gui.UIAnchorWidget(
                anchor_x='center_x',
                anchor_y='center_y',
                align_y=0,
                child=self.v_box))

#BUTTON CLICKS
        @green.event("on_click")
        def on_click_flatbutton(event):
            self.options['color']='green'
            color_choice.texture=arcade.load_texture("src/images/chosen/green_choice.png")
            start_game.texture= arcade.load_texture('src/images/buttons/start_g.png')
            start_game.texture_hovered= arcade.load_texture('src/images/buttons/start_green_clicked.png')

        @blue.event("on_click")
        def on_click_flatbutton(event):
            self.options['color']='blue'
            color_choice.texture=arcade.load_texture("src/images/chosen/blue_choice.png")
            start_game.texture= arcade.load_texture('src/images/buttons/start_b.png')
            start_game.texture_hovered= arcade.load_texture('src/images/buttons/start_blue_clicked.png')

        @white.event("on_click")
        def on_click_flatbutton(event):
            self.options['color']='white'
            color_choice.texture=arcade.load_texture("src/images/chosen/white_choice.png")
            start_game.texture= arcade.load_texture('src/images/buttons/start_w.png')
            start_game.texture_hovered= arcade.load_texture('src/images/buttons/start_white_clicked.png')

        @yellow.event("on_click")
        def on_click_flatbutton(event):
            self.options['color']='yellow'
            color_choice.texture=arcade.load_texture("src/images/chosen/yellow_choice.png")
            start_game.texture= arcade.load_texture('src/images/buttons/start_y.png')
            start_game.texture_hovered= arcade.load_texture('src/images/buttons/start_yellow_clicked.png')

        @level_beginner.event("on_click")
        def on_click_flatbutton(event):
            self.options['level']='beginner'
            level_choice.texture=arcade.load_texture("src/images/chosen/beginner_choice.png")

        @level_intermediate.event("on_click")
        def on_click_flatbutton(event):
            self.options['level']='intermediate'
            level_choice.texture=arcade.load_texture("src/images/chosen/intermediate_choice.png")

        @level_expert.event("on_click")
        def on_click_flatbutton(event):
            self.options['level']='expert'
            level_choice.texture=arcade.load_texture("src/images/chosen/expert_choice.png")

        @start_game.event("on_click")
        def on_click_flatbutton(event):
            print(self.options)
            print("Starting Game")
            game_view= game.GameView(self.options)
            self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, self.background)
        self.manager.draw()
