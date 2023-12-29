from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle

class Settings(Screen):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)

        # Set the initial background color
        self.background_color = Color(1, 1, 1, 1)  # White color initially

        # Create sliders for RGB and Alpha components
        self.red_slider = Slider(min=0, max=1, value=self.background_color.r)
        self.green_slider = Slider(min=0, max=1, value=self.background_color.g)
        self.blue_slider = Slider(min=0, max=1, value=self.background_color.b)
        self.alpha_slider = Slider(min=0, max=1, value=self.background_color.a)

        # Create an "Apply" button
        apply_button = Button(text="Apply", on_press=self.apply_settings)

        # Create a label to display current settings
        self.label = Label(text="Background Color: RGBA(1, 1, 1, 1)")

        # Add widgets to the layout
        settings_layout = BoxLayout(orientation='vertical')
        settings_layout.add_widget(self.red_slider)
        settings_layout.add_widget(self.green_slider)
        settings_layout.add_widget(self.blue_slider)
        settings_layout.add_widget(self.alpha_slider)
        settings_layout.add_widget(apply_button)
        settings_layout.add_widget(self.label)
        self.add_widget(settings_layout)

    def apply_settings(self, instance):
        # Update the background color based on slider values
        self.background_color.r = self.red_slider.value
        self.background_color.g = self.green_slider.value
        self.background_color.b = self.blue_slider.value
        self.background_color.a = self.alpha_slider.value

        # Update the label text
        self.label.text = f"Background Color: RGBA({self.background_color.r}, {self.background_color.g}, {self.background_color.b}, {self.background_color.a})"

        # Clear the canvas before applying the background color
        self.canvas.before.clear()

        # Apply the background color to the canvas
        with self.canvas.before:
            self.background_color
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Dismiss the settings screen
        self.manager.current = 'main'

# Assuming red_slider, green_slider, blue_slider, and alpha_slider are defined globally
