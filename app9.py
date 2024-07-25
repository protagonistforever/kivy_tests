from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
class App9(MDApp):
    def build(self):
        self.theme_cls.primary_palette="DeepPurple"
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_hue="A700"
        return MDRectangleFlatButton(text="THEME>>>",
                            pos_hint={"center_x":0.5,"center_y":0.5})
App9().run()