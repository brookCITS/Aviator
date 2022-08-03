import arcade
import sys
#import src.views
sys.path.insert(0, 'src/views')

import menu


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
      self.options = {
            'color': 'green', 'white', 'blue', 'yellow'
            'level': 'beginner', 'intermediate', 'advanced'
        }   


    def on_show_view(self):
     return super().on_show_view()


    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.manager.draw()
        
   @greenbutton.event("on_click")
   def on_click_flatbutton(event):
        self.options['color'] = 'green'
        
   @whitebutton.event("on_click")
   def on_click_flatbutton(event):
        self.options['color'] = 'white
        
    @bluebutton.event("on_click")
   def on_click_flatbutton(event):
        self.options['color'] = 'blue'
        
    @yellowbutton.event("on_click")
   def on_click_flatbutton(event):
        self.options['color'] = 'yellow'
        
    @beginnerbutton.event("on_click")
   def on_click_flatbutton(event):
        self.options['level'] = 'beginner'
        
   @intermediatebutton.event("on_click")
   def on_click_flatbutton(event):
        self.options['level'] = 'intermediate'
        
   @advancedbutton.event("on_click")
   def on_click_flatbutton(event):
        self.options['level'] = 'advanced'
        
    
    
