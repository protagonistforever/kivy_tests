from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
class HelloApp(MDApp):
    def build(self):
        txt=MDLabel(text="Kazama>>",halign='center',font_style="H1"
                    ,theme_text_color='Custom',text_color=(212/255.0,144/255.0,171/255.0,1))
        return txt
HelloApp().run()