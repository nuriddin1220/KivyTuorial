from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('progress.kv')

class MyLayout(Widget):
    def press_it(self):
        current=self.ids.my_progressbar.value
        if current ==1:
            current=0
        current+=0.25
        self.ids.my_progressbar.value=current
        self.ids.my_label.text=f'{current*100}% Progress'

class AwesomeApp(App):
    def build(self):
        return MyLayout()
 

 
if __name__ == '__main__':
    AwesomeApp().run()
