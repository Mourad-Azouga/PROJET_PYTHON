#all kivy app codes will be here
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
Window.clearcolor = (0.7, 0.7, 1, 1)

class main(App):
    def build(self):
        r = FloatLayout()
        self.title = 'TIMEXI - Gestion Emploi Du Temps'
        self.icon = "download.png"
        test = Image (
            source = 'download.png',
            size_hint = (.6, 0.3),
            pos_hint = {'x': 0, 'y': .7},
        )
        test2 = Image (
            source = 'download.png',
            size_hint = (.6, 0.3),
            pos_hint = {'x': .5, 'y': .7}
        )
        test3 = Image (
            source = 'download.png',
            size_hint = (.6, 0.3),
            pos_hint = {'x': .0, 'y': .4}
        )
        r.add_widget(test)
        r.add_widget(test2)
        r.add_widget(test3)
        return r
if __name__ == '__main__':
    main().run()