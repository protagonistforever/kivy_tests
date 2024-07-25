from kivymd.app import MDApp
from kivymd.uix.label import MDIcon
from kivymd.uix.button import MDFlatButton,MDFillRoundFlatButton,MDIconButton,MDFloatingActionButton
class ButtonApp(MDApp):
    def build(self):
        btn= MDFlatButton(text='KAzama',pos_hint={"center_x":0.5,"center_y":0.5})
        btn2=MDFillRoundFlatButton(text='KAzama',pos_hint={"center_x":0.5,"center_y":0.5})
        btn3=MDIconButton(icon="android",pos_hint={"center_x":0.5,"center_y":0.5})
        btn4=MDFloatingActionButton(icon="android",pos_hint={"center_x":0.5," center_y":0.5})
        return btn4
ButtonApp().run()
