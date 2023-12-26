from header import *
from kivy.graphics import Color, Rectangle

class Settings(Screen):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)

        # Set the background color to black
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Black color (RGB values in the range [0, 1])
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Bind the update of background size and position to the screen size and position
        self.bind(size=self._update_rect, pos=self._update_rect)

        amphi_layout = BoxLayout(orientation='vertical')
        amphi_layout.add_widget(Button(text="Close", on_press=self.dismiss))
        self.add_widget(amphi_layout)

    def _update_rect(self, instance, value):
        # Update the background size and position when the screen size or position changes
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def dismiss(self, instance):
        self.manager.current = 'main'
