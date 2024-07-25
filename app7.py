from kivymd.app import MDApp
from kivymd.uix.label import MDIcon
from kivy.uix.anchorlayout import AnchorLayout
from torch import layout
class MyApp(MDApp):
    def build(self):
        layout=AnchorLayout()
        ic=MDIcon(icon="fingerprint",halign="center")
        layout.add_widget(ic)
        return layout
MyApp().run()