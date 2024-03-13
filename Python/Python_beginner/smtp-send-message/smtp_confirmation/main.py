from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests


"""
## to start send confirmation line . need to start first flask in the file app.py created self . and than  rund gui kivy
"""


class RegistrationApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.email_input = TextInput(hint_text='Enter your email')
        self.register_button = Button(text='Register', on_press=self.register)

        self.layout.add_widget(self.email_input)
        self.layout.add_widget(self.register_button)

        return self.layout

    def register(self, instance):
        email = self.email_input.text

        if email:
            response = requests.post('http://localhost:5000/register', data={'email': email})
            self.layout.add_widget(TextInput(text=response.text, readonly=True))

if __name__ == '__main__':
    RegistrationApp().run()