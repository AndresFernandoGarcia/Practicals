

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKmApp(App):


    def build(self):
        """ Build the Kivy app from the kv file. """
        Window.size = (400, 200)
        self.title = "Miles to Kilometer converter"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        correct = validate_input(value)

        if (correct == False):
            result = "Your number must be an integer!"
            self.root.ids.input_number.text = str(0)


        else:
            value = int(value)
            if (value < 0):
                result = "Value must be greater than 0!"
                self.root.ids.input_number.text = str(0)

            else:
                result = value * 1.609
        self.root.ids.output_label.text = str(result)




    def handle_increment(self, value, increment):
        """ Handles increment of input value """

        correct = validate_input(value)

        if(correct == False):
            self.root.ids.output_label.text = str("Your number must be an integer!")
            result = 0

        else:
            value = int(value)
            if(value <= 0 and increment == -1):
                result = 0
            else:
                result = value + increment

        self.root.ids.input_number.text = str(result)


def validate_input(value):
    """ Function that validates that input isn't empty and is an integer """
    try:
        value = int(value)

        if(value == ""):
            return False


    except ValueError:
        return False

MilesToKmApp().run()