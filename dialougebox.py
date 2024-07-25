from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
class MyDialogbox(MDApp):
    def build(self):
        close_btn=MDFlatButton(text="close",on_release=self.close_dial)
        more_btn=MDFlatButton(text="more",on_release=self.more_fun)
        self.dialog=MDDialog(title="Notice"
                             ,text="this is a test notice"
                             ,size_hint=(0.7,1)
                             ,buttons=[close_btn,more_btn])
        self.dialog.open()
    def close_dial(self,obj):
        self.dialog.dismiss()
    def more_fun(self,obj):
        pass
MyDialogbox().run()