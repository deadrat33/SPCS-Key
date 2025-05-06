from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SPCSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.northing_input = TextInput(hint_text='Enter Northing (US survey feet)', multiline=False, input_filter='float')
        self.easting_input = TextInput(hint_text='Enter Easting (US survey feet)', multiline=False, input_filter='float')
        
        self.result_label = Label(text='Result will appear here')
        
        check_button = Button(text='Check Zone')
        check_button.bind(on_press=self.check_zone)
        
        clear_button = Button(text='Clear')
        clear_button.bind(on_press=self.clear_inputs)
        
        layout.add_widget(self.northing_input)
        layout.add_widget(self.easting_input)
        layout.add_widget(check_button)
        layout.add_widget(clear_button)
        layout.add_widget(self.result_label)
        
        return layout

    def check_zone(self, instance):
        try:
            northing = float(self.northing_input.text)
            easting = float(self.easting_input.text)
            result = self.lookup_zone(easting, northing)
            self.result_label.text = f"Result: {result}"
        except:
            self.result_label.text = "Invalid input."

    def clear_inputs(self, instance):
        self.northing_input.text = ''
        self.easting_input.text = ''
        self.result_label.text = 'Result will appear here'

    def lookup_zone(self, easting, northing):
        zones = [
            {"name": "Texas North", "min_e": 1968500.0, "max_e": 2624675.0, "min_n": 656166.7, "max_n": 2296583.3},
            {"name": "Texas North Central", "min_e": 1968500.0, "max_e": 2624675.0, "min_n": 492125.0, "max_n": 1640416.7},
            {"name": "Texas Central", "min_e": 1968500.0, "max_e": 2624675.0, "min_n": 328083.3, "max_n": 1312333.3},
            {"name": "Texas South Central", "min_e": 1968500.0, "max_e": 2624675.0, "min_n": 164041.7, "max_n": 984250.0},
            {"name": "Texas South", "min_e": 1968500.0, "max_e": 2624675.0, "min_n": 0.0, "max_n": 656166.7},
        ]
        for zone in zones:
            if zone["min_e"] <= easting <= zone["max_e"] and zone["min_n"] <= northing <= zone["max_n"]:
                return zone["name"]
        return "Coordinate not in any Texas SPCS zone."

if __name__ == '__main__':
    SPCSApp().run()