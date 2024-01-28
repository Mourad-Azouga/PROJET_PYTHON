from header import *
from amphi_screen import AmphiScreen, AmphiFinal
from salle_screen import SalleScreen, SalleSections
from confi_screen import ConfiScreen

Window.clearcolor = (238/255, 238/255, 238/255, 1)
Window.size = (1200,600)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        header_background = Image(source='back.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(header_background)
    
        main_layout = BoxLayout(orientation='vertical')

        header = RelativeLayout()

        quit_ = Button(
            background_normal='3.png',
            background_down='3.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': .85},
            padding=(10, 0, 10, 0)
        )

        quit_.bind(on_press=self.quit_)
        header.add_widget(quit_)
        main_layout.add_widget(header)

        #main buttons
        main_buttons = BoxLayout(
            orientation='horizontal',
            padding=(30, 30, 30, 100),
            spacing=30,
        )

        amphi_button = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(500, 250),
            size_hint=(.8, .8),
            pos_hint={'x': 0, 'y': 0}
        )
        amphi_button.bind(on_press=self.amphi_button_press)

        salles_button = Button(
            background_normal='2.png',
            background_down='2.png',
            size=(500, 250),
            size_hint=(.8, .8),
            pos_hint={'x': 0, 'y': 0}
        )
        salles_button.bind(on_press=self.salle_button_press)

        confi_button = Button(
            background_normal='confi.png',
            background_down='confi.png',
            size=(500, 250),
            size_hint=(.8, .8),
            pos_hint={'x': 0, 'y': 0}
        )
        confi_button.bind(on_press=lambda instance: self.confi_button_press(instance, 'Salle F'))

        main_buttons.add_widget(amphi_button)
        main_buttons.add_widget(salles_button)
        main_buttons.add_widget(confi_button)

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
    
    def confi_button_press(self, instance,salle_name):
        screen_manager = self.manager
        salle_final_screen = self.manager.get_screen('salle_sections')
        salle_final_screen.set_salle_section(salle_name)
        transition = SlideTransition(direction='left')
        self.manager.transition = transition
        self.manager.current = 'confi_screen'

    def quit_(self, instance):
        MainApp().stop()

class MainApp(App):
    def build(self):
        room.load_reservations("data.json")
        self.title = 'TIMEXI - Gestion Emploi Du Temps'
        screen_manager = ScreenManager()

        main_screen = MainScreen(name='main')
        amphi_screen = AmphiScreen(name='amphi')
        salle_screen = SalleScreen(name='salle')
        amphi_final = AmphiFinal(name='amphi_final')
        salle_sections = SalleSections(name='salle_sections')
        confi_screen = ConfiScreen(name='confi_screen')




        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(amphi_screen)
        screen_manager.add_widget(salle_screen)
        screen_manager.add_widget(amphi_final)
        screen_manager.add_widget(salle_sections)
        screen_manager.add_widget(confi_screen)

        return screen_manager



if __name__ == '__main__':
    MainApp().run()
