from random import random
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line



class DrawInput(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1., 1.)
        with self.canvas:
            Color(*color, mode='hsv')
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=2)
        
    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)
		
    def on_touch_up(self, touch):
        print("RELEASED!",touch)


class SimpleKivy4(App):
    
    def build(self):
        parent = Widget()
        self.painter = DrawInput()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
      self.painter.canvas.clear()

if __name__ == "__main__":
    Window.fullscreen = True
    SimpleKivy4().run()