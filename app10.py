from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton
class TextApp(MDApp):
    def build(self):
        layout=MDBoxLayout(orientation="vertical",spacing=10,padding=250)
        txt=MDTextField(text="Email or Username ",pos_hint={"center_x":0.5,"center_x":0.5})
        btn=MDRectangleFlatIconButton(text="LogIn",pos_hint={"center_x":0.5,"center_x":0.5})
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout
TextApp().run()

