from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screen import Screen
style="""
MDBoxLayout:
    orientation:"vertical"
    padding:90
    spacing:10
    MDTextField:
        hint_text:"Enter Username or Email"
        helper_text:"username must be unique"
        helper_text_mode:"on_focus"
        icon_left:"account"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Enter Password"
        helper_text:"Use strong password"
        helper_text_mode:"on_focus"
        icon_left:"lock-off"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        size_hint_x:None
        width:300
    MDRectangleFlatIconButton:
        text:"LogIn"
        icon: "login-variant"
        pos_hint:{"center_x":0.5,"center_y":0.5}
"""
class LoginPage(MDApp):
    def build(self):
        scn=Screen()
        bd=Builder.load_string(style)
        scn.add_widget(bd)
        return scn
LoginPage().run()

