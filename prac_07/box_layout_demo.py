from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("Greeted...")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text
        self.root.ids.output_label.color = (1, 1, 1, 1)

    def handle_clear(self):
        print("Cleared...")
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.output_label.color = (1, 1, 0, 1)
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
