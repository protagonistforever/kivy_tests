from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file('./calculator.kv')
Window.size = (350, 550)

class CalculatorWidget(Widget):
    # Clear the screen
    def clear(self):
        self.ids.input_box.text = "0"

    # Remove the last character
    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    # Getting the button value
    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if "wrong equation" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"

        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    # Getting the sings
    def sings(self, sing):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sing}"

    # Getting decimal value
   # Getting decimal value
# Getting decimal value
    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split("\+|\*|-|/|%", prev_number) # type: ignore

        if "%" in num_list[-1] and "." not in num_list[-1]:
            # Convert the percentage to its decimal equivalent
            percentage_value = float(num_list[-1].strip("%")) / 100.0
            prev_number = f"{prev_number}{percentage_value}."  # Add decimal point
            self.ids.input_box.text = prev_number

        elif "." in prev_number:
            pass

        else:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number


    # Calculate the result
    def results(self):
        prev_number = self.ids.input_box.text
        try:
            result = eval(prev_number)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "wrong equation"

    # Positive to negative
    def positive_negative(self):
        prev_number = self.ids.input_box.text
        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == "__main__":
    CalculatorApp().run()