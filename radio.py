from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


# Designate Our .kv design file 
Builder.load_file('radio.kv')

class MyLayout(Widget):
    checks=[]
    def checkbox_click(self,instance,value,topping):
        if value == True:
            MyLayout.checks.append(topping)
            tops=''
            for i in MyLayout.checks:
                tops+=i+' '
            self.ids.output_label.text=f'You selected: {tops}'
        else:
            MyLayout.checks.remove(topping)
            tops=''
            for i in MyLayout.checks:
                tops+=i+' '
            self.ids.output_label.text=f'You selected: {tops}'
            
	
 
class AwesomeApp(App):
    def build(self):
        return MyLayout()

 
if __name__ == '__main__':
    AwesomeApp().run()
