from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Converter(App):
    def build(self):
        Window.size = (700, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('my_miles_to_km_converter.kv')
        return self.root

    def handel_convert(self, value):
        try:
            print("Converting...{}".format(value))
            result = float(value) * 1.609
        except ValueError:
            print("ValueError")
            result = 0.0
        self.root.ids.output_label.text = str(result)

    def handel_increment(self, value):
        try:
            print("Incrementing...{}".format(value))
            self.root.ids.input_number.text = str(float(self.root.ids.input_number.text) + value)
        except ValueError:
            self.root.ids.input_number.text = str(0 + float(value))


Converter().run()
