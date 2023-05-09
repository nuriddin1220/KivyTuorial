from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import kivy
from kivy.config import Config

kivy.require('2.0.0')
Config.set('graphics', 'backend', 'sdl2')

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
        #Test for error first
        if "Error" in prior:
            prior=''
        #if determine if the zero sitting
        if prior=='0':
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{button}'
        else:
            self.ids.calc_input.text=f'{prior}{button}'
    
    #lets create addition function
    def math_sign(self,sign):
        #create a variable that contains whatever in textbox
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}{sign}'
    
    def remove(self):
        prior=self.ids.calc_input.text
        prior=prior[:-1]
        self.ids.calc_input.text=prior

    def pos_neg(self):
        prior=self.ids.calc_input.text
        
        if "-" in prior:
            self.ids.calc_input.text=f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text=f'-{prior}'


    def dot(self):
        prior=self.ids.calc_input.text
        #add a period decimal to the end of the text
        num_list=prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            prior=f'{prior}.'
            #output back to the text box
            self.ids.calc_input.text=prior
        elif   "." in prior:
            pass
        else:
            prior=f'{prior}.'
            #output back to the text box
            self.ids.calc_input.text=prior

    #create equals to function
    def equals(self):
        prior=self.ids.calc_input.text
        #Error handling
        try:    
            #evaluate text from textbox
            answer=eval(prior)
            # output the answer
            self.ids.calc_input.text=str(answer)
        except:
            self.ids.calc_input.text='Error'


        #Adding 
        # if "+" in prior:
        #     num_list=prior.split("+")
        #     print(num_list)
        #     answer=0.0

        #     #loop thru list
        #     for number in num_list:
        #         answer=answer+float(number)
        #     self.ids.calc_input.text=str(answer)

    
    
class CalculatorApp(App):
    def build(self):
        return MyLayout()

    
if __name__ == '__main__':
    CalculatorApp().run()