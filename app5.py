from kivy.app import App
from kivy.uix.image import Image,AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.clearcolor=(0.6,0,0.5,1)
Window.size=(330,520)
class MyButton(App):
    def build(self):
        layout=BoxLayout(orientation="vertical",spacing=10,padding=100)
        btn1=Button(text="button 1")
        btn2=Button(text="button 2")
        btn3=Button(text="button 3")
        btn4=Button(text="button 4")
        btn5=Button(text="button 5")
        btn6=Button(text="button 6")
        btn7=Button(text="button 7")
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)
        layout.add_widget(btn7)
        return layout
MyButton().run()