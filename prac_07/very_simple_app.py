from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class SimpleApp(App):
    def __init__(self):
        super().__init__()
        self.names = ["Matthew", "Mark", "Luke", "Leia"]

    def build(self):
        self.title = "A very simple app"
        self.root = Builder.load_file('very_simple_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


SimpleApp().run()
