from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

"""
class MyWidgets(GridLayout):

    def __int__(self, **kwargs):
        super(self, MyWidgets).__init__(**kwargs)
        self.Button = Button
        self.TextIntput = TextInput
        self.Label = Label
        self.GridLayout = GridLayout
        self.BoxLayout = BoxLayout
"""


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        b1 = Button(text="firstB")
        b2 = Button(text="SecondB")
        b3 = Button(text="thirdB")
        # label = Label(text="feri label")
        # textinput = TextInput(text="")
        # scroler = ScrollView(text="scroll window")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        # self.add_widget(textinput)
        # self.add_widget(label)
        # self.add_widget(scroler)


"""
        # -----------Create a TextInput widget
        #text_input = TextInput(hint_text="Type here")

        # ------------Bind the on_text event to the capture_input method
        text_input.bind(on_text=self.capture_input)

    def capture_input(self, instance, value):
        # --------This method is called whenever the TextInput's text changes
        # ------------Append the input value to the input_values list
        input_values.append(value)
        print("Input Value:", value)

"""


class ResizableLabel(Label):
    max_font_size= 15

    def on_width(self, instance, value):
        self.font_size = min(value, self.max_font_size)
        if value < self.max_font_size:
           self.font_size = value
        else:
            self.font_size = self.max_font_size



class ResizableLabel2(Label):
    max_font_size = 20 # Define your maximum font size here

    def on_width(self, instance, value):
        if value < self.size[0]:
            self.font_size = max(value * 0.5, self.max_font_size)
        else:
            self.font_size = self.max_font_size







    # def __getattr__(name):
    # pass


class MainWidget(Widget):

    def access_element(self, ):
        liste1 = []
        input_value = self.root.ids.text_input
        if input_value == True:
            liste1.append(input_value)


class MyApplicationApp(App):


    def get_input_value(self):
        input_values_list = {}

        input_values_list['vor_name'] = self.root.ids.vor_name.text
        v_name = input_values_list['vor_name']

        input_values_list['nach_name'] = self.root.ids.nach_name.text
        n_name = input_values_list['nach_name']

        input_values_list['emailaddress'] = self.root.ids.emailaddress.text
        email_addres = input_values_list['emailaddress']

        input_values_list['repeatemail'] = self.root.ids.repeatemail.text
        repeat_email = input_values_list['repeatemail']
        #print("vor name: ", v_name)
        #print("nachname : ", n_name)
        #print("email: ", email_addres)
        #print("reapeat email: ", repeat_email)

        # new list als dictionary
        new_dictoinary = {"Vor Name": v_name, "Nach Name": n_name, "email": email_addres, "Repeat Eamail": repeat_email}
        print("Here is a dictionary of inputs: ",new_dictoinary)

        # new list and add elements into it
        new_list = []
        new_list.append(v_name)
        new_list.append(n_name)
        new_list.append(email_addres)
        new_list.append(repeat_email)
        print("Here is information list of registeration :",new_list)




    def build(self):

        """
        # get values from inputtext of app.kv files
        def get_input_value(instance):

            input_text = instance.text
            input_values.append(input_text)
            #values = input_text
            print("Input Value: ",input_text)
            print("Input Value: ",input_values)
            button = Button(text="Get Input Value")
            button.bind(on_release=get_input_value)

        """
        # windows size
        Window.size = (400, 500)
        #label = ResizableLabel(text="Resizeable Font size")

        # Calculate the position for the top-right corner
        screen_width = Window.width
        screen_height = Window.height
        window_width = -715
        window_height = 567
        top = screen_height - window_height
        right = screen_width - window_width

        # Set the window position to the top-right corner
        Window.top = top
        Window.left = right

        return BoxLayoutExample()


if __name__ == "__main__":
    MyApplicationApp().run()