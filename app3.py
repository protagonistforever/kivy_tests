from kivy.app import App
from kivy.uix.image import Image,AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
class MyImage(App):
    def build(self):
        img=Image(source=r"C:\Users\PRADE\OneDrive\Desktop\National_Institute_of_Technology,_Nagaland_Logo.png")
        return img
MyImage().run()
