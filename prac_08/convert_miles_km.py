from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERTION_RATE = 1.609344

class ConvertMilesToKilometersApp(App):
    """An app that converts miles to kilometers."""
    message = StringProperty()
    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles To Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = ""
        return self.root


    def handle_calculation(self, modification=0):
        """Handle calculation (could be button press or other call), output result to self.message."""
        number_of_miles = self.get_valid_float() + modification
        self.message = str(MILES_TO_KM_CONVERTION_RATE * number_of_miles)
        if modification!= 0:
            self.root.ids.user_input.text = str(int(number_of_miles)) if number_of_miles.is_integer() else str(number_of_miles)

    def get_valid_float(self):
        """Get a valid float, return 0.0 if it's an invalid input."""
        try:
            input_float = float(self.root.ids.user_input.text)
            return input_float
        except ValueError:
            return 0.0


ConvertMilesToKilometersApp().run()