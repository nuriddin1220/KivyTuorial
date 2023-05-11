from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window



# Designate Our .kv design file 
Builder.load_file('split.kv')
class MyLayout(Widget):
    def spinner_clicked(self,value):
        self.ids.click_label.text = f'you selected {value}'
	
 
class AwesomeApp(App):
    def build(self):
        return MyLayout()
 
 
 
if __name__ == '__main__':
    AwesomeApp().run()
