from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
    
    pass
    
class MenuWindow(Screen):
    def __init__(self, **kwargs):
        super(MenuWindow, self).__init__(**kwargs)
        self.option1=ObjectProperty(None)
        self.option2=ObjectProperty(None)
        self.option3=ObjectProperty(None)
        
    def parse_option(self, text):
        if "@" in text and "." in text:
            return True
        else:
            return False
    pass
    
class TopBar(GridLayout):
    def __init__(self, **kwargs):
        super(TopBar, self).__init__(**kwargs)        
        self.LOADING = 0
        self.link="menu"
        
    def button_mid(self):
        #print("text: ", instance.text)
        #print("id: ", instance.id)
        print("1")
        
    def button_menu(self):
        if .current=="menu":
            print(root.current)
            print(" pressed")
            self.link = "main"
        else:
            print(root.current)
            print(" pressed")
            self.link = "menu"

    def button_right(self):
        print("Right button pressed")

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return kv
        

kv = Builder.load_file("my.kv")

if __name__ == "__main__":
    MainApp().run()
