from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build the box layout demo app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet button press, display greeting message."""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle clear button press, clear input file, change label prompt."""
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""

BoxLayoutDemo().run()
