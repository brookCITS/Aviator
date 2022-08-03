import arcade
import arcade.gui
import sys
sys.path.insert(0, 'src/views')
#import views
import A

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.options = {
            'color': 'green',
            'level': 'beginner'
            }

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
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
        title_label = arcade.gui.UITextArea(text="Aviator", text_color=arcade.color.RED, font_size=60, font_name="FFF Tusj")
        title_label.fit_content()

    #COLOR CHOOSE
        color_choose_text = arcade.gui.UILabel(text='CHOOSE A COLOR')
        color_choose_text.fit_content()

    #COLORS
        green = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('src/images/planes/green.png'), texture_hovered=arcade.load_texture('src/images/planes/green_clicked.png'), scale=2)
        blue = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('src/images/planes/blue.png'), texture_hovered=arcade.load_texture('src/images/planes/blue_clicked.png'), scale=2)
        white = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('src/images/planes/white.png'), texture_hovered=arcade.load_texture('src/images/planes/white_clicked.png'), scale=2)
        yellow = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture('src/images/planes/yellow.png'), texture_hovered=arcade.load_texture('src/images/planes/yellow_clicked.png'), scale=2)

    #LEVEL CHOOSE
        level_choose_text = arcade.gui.UILabel(text='CHOOSE A DIFFICULTY LEVEL')
        level_beginner = arcade.gui.UITextureButton(texture=arcade.load_texture('src/images/buttons/beginner.png'), texture_hovered=arcade.load_texture('src/images/buttons/beginner_clicked.png'), scale=.8)
        level_intermediate = arcade.gui.UITextureButton(texture=arcade.load_texture('src/images/buttons/intermediate.png'), texture_hovered=arcade.load_texture('src/images/buttons/intermediate_clicked.png'), scale=.8)
        level_expert = arcade.gui.UITextureButton(texture=arcade.load_texture('src/images/buttons/expert.png'), texture_hovered=arcade.load_texture('src/images/buttons/expert_clicked.png'), scale=.8)

    #FINAL CHOICE
        color_choice = arcade.gui.UILabel(text="GREEN", width=150, align='center')
        level_choice = arcade.gui.UILabel(text="BEGINNER", width=150, align='center')

    #START
        start_game = arcade.gui.UITextureButton(texture= arcade.load_texture('src/images/buttons/start_g.png'), texture_hovered=arcade.load_texture('src/images/buttons/start_green_clicked.png'), scale=.7)

#CODE THAT ADDS TO DISPLAY
#-------------------------
#GAME TITLE
        self.v_box.add(title_label.with_border(width=0, color=arcade.color.BLACK).with_space_around(bottom=50))

#COLOR CHOOSE
        self.v_box.add(color_choose_text.with_space_around(bottom=10))
    #COLORS
        self.h_box.add(green.with_space_around(right=10))
        self.h_box.add(blue.with_space_around(right=10))
        self.h_box.add(white.with_space_around(right=10))
        self.h_box.add(yellow)
        self.v_box.add(self.h_box.with_space_around(bottom=10))

#LEVEL CHOOSE
        self.v_box.add(level_choose_text.with_space_around(bottom=10, top=30))
    #LEVELS
        self.h_box2.add(level_beginner.with_space_around(right=10, bottom=10))
        self.h_box2.add(level_intermediate.with_space_around(right=10, bottom=10))
        self.h_box2.add(level_expert.with_space_around(bottom=10))
        self.v_box.add(self.h_box2)

#CHOICES
        self.h_box3.add(color_choice.with_space_around(right=20, bottom=10))
        self.h_box3.add(level_choice.with_space_around(bottom=10))
        self.v_box.add(self.h_box3.with_space_around(top=50))

#START BUTTON
        self.v_box.add(start_game.with_space_around(top=10))

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
            color_choice.text="GREEN"
            start_game.texture= arcade.load_texture('src/images/buttons/start_g.png')
            start_game.texture_hovered= arcade.load_texture('src/images/buttons/start_green_clicked.png')

        @blue.event("on_click")
        def on_click_flatbutton(event):
            self.options['color']='blue'
            color_choice.text="BLUE"
            start_game.texture= arcade.load_texture('src/images/buttons/start_b.png')
            start_game.texture_hovered= arcade.load_texture('src/images/buttons/start_blue_clicked.png')

        @white.event("on_click")
        def on_click_flatbutton(event):
            self.options['color']='white'
            color_choice.text="WHITE"
            start_game.texture= arcade.load_texture('src/images/buttons/start_w.png')
            start_game.texture_hovered= arcade.load_texture('src/images/buttons/start_white_clicked.png')

        @yellow.event("on_click")
        def on_click_flatbutton(event):
            self.options['color']='yellow'
            color_choice.text="YELLOW"
            start_game.texture= arcade.load_texture('src/images/buttons/start_y.png')
            start_game.texture_hovered= arcade.load_texture('src/images/buttons/start_yellow_clicked.png')

        @level_beginner.event("on_click")
        def on_click_flatbutton(event):
            self.options['level']='beginner'
            level_choice.text="BEGINNER"

        @level_intermediate.event("on_click")
        def on_click_flatbutton(event):
            self.options['level']='intermediate'
            level_choice.text="INTERMEDIATE"

        @level_expert.event("on_click")
        def on_click_flatbutton(event):
            self.options['level']='expert'
            level_choice.text="EXPERT"

        @start_game.event("on_click")
        def on_click_flatbutton(event):
            print(self.options)
            print("Starting Game")
            game_view= game.GameView(self.options)
            self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()
