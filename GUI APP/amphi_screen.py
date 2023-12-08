# File: Amphi_screen.py
from header import *
from kivy.app import App  
class AmphiScreen(Screen):
    def __init__(self, **kwargs):
        super(AmphiScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical', size_hint =(1,1),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #header how l "div" li 3amlin fih les buttons dial shutdown w dakchi
        header = BoxLayout(orientation='vertical', size_hint=(None, .1))

        quit_ = Button(
            background_normal='3.png',
            background_down='3.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint = {'x': 0, 'y':0},
            padding=(10, 0, 10, 0)
        )
        quit_.bind(on_release = self.quit_)

        settings = Button(
            background_normal='4.png',
            background_down='4.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint = {'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        settings.bind(on_press=self.settings)

        back_to_main = Button(
            background_normal='5.png',
            background_down='5.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint = {'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        back_to_main.bind(on_press=self.dismiss)
        quit_.bind(on_press=self.quit_)
        header.add_widget(back_to_main)
        header.add_widget(settings)
        header.add_widget(quit_)

        #hna kanbdaw b les buttons
        main_buttons_1 = BoxLayout(
            orientation='horizontal',
            padding=(30, 0, 0, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint = {'x': 0.1, 'y': 1}
        )

        SALLE_A = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        SALLE_B = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        main_buttons_1.add_widget(SALLE_A)
        main_buttons_1.add_widget(SALLE_B)
        main_layout.add_widget(main_buttons_1)

        main_buttons_2 = BoxLayout(
            orientation='horizontal',
            padding=(30, 0, 0, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint = {'x': 0.1, 'y': 0}
        )

        SALLE_E = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint =(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        SALLE_F = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        main_buttons_2.add_widget(SALLE_E)
        main_buttons_2.add_widget(SALLE_F)
        main_layout.add_widget(main_buttons_2)
        main_buttons_3 = BoxLayout(
            orientation='horizontal',
            padding=(30, 0, 0, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint = {'x': 0.1, 'y': 0}
        )

        SALLE_E = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint =(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        SALLE_F = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        main_buttons_3.add_widget(SALLE_E)
        main_buttons_3.add_widget(SALLE_F)

        main_layout.add_widget(main_buttons_3)
        main_layout.add_widget(header)






        self.add_widget(main_layout)

    def dismiss(self, instance):

        transition = SlideTransition(direction='right')
        self.manager.transition = transition
        self.manager.current = 'main'

    def settings(self, instance):
        self.manager.current = 'settings'

    def quit_(self, instance):
        App.get_running_app().stop()
