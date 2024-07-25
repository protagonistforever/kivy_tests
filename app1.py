from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
Window.clearcolor=(1,1,0.2,1)
class Myapp(App):
    def build(self):
        label=Label(text="Welcome" , font_size='120sp',bold=True,color=(0.6,0,0.5,1))
        return label
Myapp().run()
