from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen


#define our different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv=Builder.load_file('new_window.kv')

class AwesomeApp(App):
    def build(self):
        return kv
 
 
 
if __name__ == '__main__':
    AwesomeApp().run()
