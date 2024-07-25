from kivymd.app import MDApp
from kivymd.uix.list import MDList,OneLineListItem
from kivymd.uix.scrollview import MDScrollView
class ListApp(MDApp):
    def build(self):
        my_scr=MDScrollView()
        mylist=MDList()
        itm=OneLineListItem(text="Kazama")
        itm1=OneLineListItem(text="Piyush")
        itm2=OneLineListItem(text="Verma")
        itm3=OneLineListItem(text="Soul")
        my_scr.add_widget(mylist)
        mylist.add_widget(itm)
        mylist.add_widget(itm1)
        mylist.add_widget(itm2)
        mylist.add_widget(itm3)
        return my_scr
    
ListApp().run()