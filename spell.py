from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling


# Designate Our .kv design file 
Builder.load_file('spell.kv')
class MyLayout(Widget):
    
    def press(self):
        #Create a new instance of spelling object
        s=Spelling()
        #select language
        s.select_language('en_US')
        #see all supported languages
        # print(s.list_languages())
        word=self.ids.word_input.text
        option=s.suggest(word)
        x=''
        for item in option:
            x=f'{x} {item}'
        #update lable
        self.ids.word_label.text=f'{x}'

	
 
class AwesomeApp(App):
    def build(self):
        return MyLayout()
 
 
 
if __name__ == '__main__':
    AwesomeApp().run()
