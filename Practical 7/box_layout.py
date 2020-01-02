from kivy.app import App
from kivy.lang import Builder

"""
Comments with # are for myself as reminders
"""
class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        # changing label text and adding name greet
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_text(self):
        self.root.ids.input_name.text = " " #changing input name to blank using id's
        self.root.ids.output_label.text = ' ' #changing output label to blank using id's

BoxLayoutDemo().run()