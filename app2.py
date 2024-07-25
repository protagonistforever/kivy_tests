from kivy.app import App
from kivy.uix.button import Button
class ButtonApp(App):
    def build(self):
        return Button(text="Click Me", font_size='44sp'
                      ,pos_hint={"center_x":0.5,"center_y":0.5}
                      ,size_hint=(0.3,0.3),bold=True,color=(1,1,0.2,1)
                      ,on_press=self.btn_click
                      ,on_release=self.btn_released)
    def btn_released(self,btn):
        print("button Released.")
    def btn_click(self,btn):
        print("button click")
        
ButtonApp().run()
