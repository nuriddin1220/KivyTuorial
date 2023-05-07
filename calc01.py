from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

#Set the app size
Window.size=(500,700)


Builder.load_file('calc.kv')
class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    #button press function
    def button_press(self,button):
        #create a variable that contains whatever in textbox
        prior=self.ids.calc_input.text
        
        #if determine if the zero sitting
        if prior=='0':
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{button}'
        else:
            self.ids.calc_input.text=f'{prior}{button}'
    
    #lets create addition function
    def add(self):
        #create a variable that contains whatever in textbox
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}+'
    
    def subtract(self):
        #create a variable that contains whatever in textbox
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}-'
        
    def multiply(self):
        #create a variable that contains whatever in textbox
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}*'
            
    def divide(self):
        #create a variable that contains whatever in textbox
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}/'    

    #create equals to function
    def equals(self):
        prior=self.ids.calc_input.text
        
        #Adding
        if "+" in prior:
            num_list=prior.split("+")
            print(num_list)
            answer=0

            #loop thru list
            for number in num_list:
                answer=answer+int(number)
            self.ids.calc_input.text=str(answer)
    
    
class CalculatorApp(App):
    def build(self):
        return MyLayout()

    
if __name__ == '__main__':
    CalculatorApp().run()