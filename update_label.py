from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder



Builder.load_file('update_label.kv')
class MyLayout(Widget):
    def press(self):
        #create variables for widget
        name=self.ids.name_input.text
        print(name)
        #update label
        self.ids.name_label.text = f'Hello {name}!'
        
        #clear input box    
        self.ids.name_input.text=''
        
        
class AwesomeApp(App):
    def build(self):
        return MyLayout()

    
if __name__ == '__main__':
    AwesomeApp().run()