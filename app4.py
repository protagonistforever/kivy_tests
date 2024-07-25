from kivy.app import App
from kivy.uix.image import Image,AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
class MyImage(App):
    def build(self):
        img=AsyncImage(source="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOQmnV_JcXPjgIId3UfkUgBlEkvaZPlcTtqD0qpWXvQA&s",size_hint=(None,None)
        ,pos_hint={"center_x":0.5,"center_y":0.5}
        )
        return img
    #def btn_close(self,btn):
     #   MyImage().close()
MyImage().run()
