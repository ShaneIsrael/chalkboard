from random import random
from kivy.app import App
from kivy.lang import Builder
# from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.uix.slider import Slider

clear_button = '''
FloatLayout:
    Button:
        text: 'CLEAR'
        font_size: 24
        size: 100, 100
        size_hint: None, None
        canvas.before:
            PushMatrix
            Rotate:
                angle: 90
                origin: self.center
        canvas.after:
            PopMatrix
'''

class DrawInput(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1., 1.)
        with self.canvas:
            Color(*color, mode='hsv')
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=3)
        
    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)
		
    def on_touch_up(self, touch):
        print("RELEASED!",touch)


class SimpleKivy4(App):
    
    def build(self):
        parent = Widget()
        self.painter = DrawInput()
        clearbtn = Builder.load_string(clear_button)
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(stroke_slider)

        return parent

    def clear_canvas(self, obj):
      self.painter.canvas.clear()

if __name__ == "__main__":
    # Window.fullscreen = True
    SimpleKivy4().run()