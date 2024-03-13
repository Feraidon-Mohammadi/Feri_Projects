from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.text_input = TextInput()
        self.layout.add_widget(self.text_input)

        self.button = Button(text='Click me!')
        self.button.bind(on_press=self.on_button_click)
        self.layout.add_widget(self.button)

        self.label = Label(text='Output will be displayed here')
        self.layout.add_widget(self.label)

        return self.layout

    def on_button_click(self, instance):
        input_text = self.text_input.text
        self.label.text = f'Output: {input_text}'

if __name__ == '__main__':
    MyApp().run()




 
"""
##############################################################################################################
########################## to show the window just thats enough ##############################################
##############################################################################################################


from kivy.app import App

class MyApp(App):
	pass
	

if __name__ == '__main__':
	MyApp().run()
	
 
 """
 
