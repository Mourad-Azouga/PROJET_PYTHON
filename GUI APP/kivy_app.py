from header import *
from kivy.app import App
from amphi_screen import AmphiScreen
from salle_screen import SalleScreen
from settings import Settings
Window.clearcolor = (1,1,1,1)
Window.size = (1060,600)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical')

        header = RelativeLayout()
        header_background = Image(source='back.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        header.add_widget(header_background)

        quit_ = Button(
            background_normal='3.png',
            background_down='3.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0.05, 'y': .85},
            padding=(10, 0, 10, 0)
        )
        settings = Button(
            background_normal='4.png',
            background_down='4.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': .85},
            padding=(30, 0, 10, 0)
        )
        settings.bind(on_press = self.settings)
        quit_.bind(on_press=self.quit_)
        header.add_widget(settings)
        header.add_widget(quit_)
        main_layout.add_widget(header)

        main_buttons = BoxLayout(
            orientation='horizontal',
            padding=(30, 30, 30, 30),
            spacing=30
        )

        amphi_button = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        amphi_button.bind(on_press=self.amphi_button_press)

        salles_button = Button(
            background_normal='2.png',
            background_down='2.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        salles_button.bind(on_press=self.salle_button_press)
        main_buttons.add_widget(amphi_button)
        main_buttons.add_widget(salles_button)
        main_layout.add_widget(main_buttons)
        self.add_widget(main_layout)

    def amphi_button_press(self, instance):
        transition = SlideTransition(direction='left')
        self.manager.transition = transition
        self.manager.current = 'amphi'

    def salle_button_press(self, instance):
        transition = SlideTransition(direction='left')
        self.manager.transition = transition
        self.manager.current = 'salle'
    def settings(self, instance):
        transition = SlideTransition(direction='left')
        self.manager.transition = transition
        self.manager.current = 'settings'

    def quit_(self, instance):
        MainApp().stop()

class MainApp(App):
    def build(self):
        self.title = 'TIMEXI - Gestion Emploi Du Temps'
        screen_manager = ScreenManager()

        main_screen = MainScreen(name='main')
        amphi_screen = AmphiScreen(name='amphi')
        salle_screen = SalleScreen(name='salle')
        settings = Settings(name='settings')

        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(amphi_screen)
        screen_manager.add_widget(salle_screen)
        screen_manager.add_widget(settings)

        return screen_manager


if __name__ == '__main__':
    MainApp().run()
