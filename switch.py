from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('switch.kv')
class MyLayout(Widget):
    def switch_click(self,switchObject,SwitchValue):
        if SwitchValue:
            self.ids.my_label.text='You Clicked Switch ON!'
        else:
            self.ids.my_label.text='You Clicked Switch OFF!'
            self.ids.my_switch.disabled = True


class AwesomeApp(App):
    def build(self):
        return MyLayout()
 

if __name__ == '__main__':
    AwesomeApp().run()
