from header import *
"""SalleScreen
    The first screen that appears after selecting the salle in the main window, in this screen the user will select the section"""
class SalleScreen(Screen):
    def __init__(self, **kwargs):
        super(SalleScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        header = BoxLayout(orientation='vertical', size_hint=(None, .1))

        quit_ = Button(
            background_normal='3.png',
            background_down='3.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': 0},
            padding=(10, 0, 10, 0)
        )
        quit_.bind(on_release=self.quit_)

        settings = Button(
            background_normal='4.png',
            background_down='4.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        settings.bind(on_press=self.settings)

        back_to_main = Button(
            background_normal='5.png',
            background_down='5.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        back_to_main.bind(on_press=self.dismiss)
        quit_.bind(on_press=self.quit_)
        header.add_widget(back_to_main)
        header.add_widget(settings)
        header.add_widget(quit_)

        main_buttons_1 = BoxLayout(
            orientation='horizontal',
            padding=(30, 30, 30, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint={'x': 0.1, 'y': 1}
        )

        SALLE_A = Button(
            background_normal='2.png',
            background_down='2.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        SALLE_A.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle A'))

        SALLE_B = Button(
            background_normal='2.png',
            background_down='2.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        SALLE_B.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle B'))

        main_buttons_1.add_widget(SALLE_A)
        main_buttons_1.add_widget(SALLE_B)
        main_layout.add_widget(main_buttons_1)

        main_buttons_2 = BoxLayout(
            orientation='horizontal',
            padding=(30, 30, 30, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint={'x': 0.1, 'y': 0}
        )

        SALLE_E = Button(
            background_normal='2.png',
            background_down='2.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        SALLE_E.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle E'))

        SALLE_F = Button(
            background_normal='2.png',
            background_down='2.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        SALLE_F.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle F'))

        main_buttons_2.add_widget(SALLE_E)
        main_buttons_2.add_widget(SALLE_F)
        main_layout.add_widget(main_buttons_2)
        main_layout.add_widget(header)

        self.add_widget(main_layout)

    def salle_button_press(self, instance, salle_name):
        # Set salle_name in Salle_Sections and transition to it
        screen_manager = self.manager
        salle_final_screen = self.manager.get_screen('salle_sections')
        salle_final_screen.set_salle_section(salle_name)
        transition = SlideTransition(direction='left')
        self.manager.transition = transition
        self.manager.current = 'salle_sections'

    def dismiss(self, instance):
        transition = SlideTransition(direction='right')
        self.manager.transition = transition
        self.manager.current = 'main'

    def settings(self, instance):
        self.manager.current = 'settings'

    def quit_(self, instance):
        App.get_running_app().stop()


"""SalleSections
    The screen that appears after selecting Salle section, now we'll need to get the salle number from our user"""
class SalleSections(Screen):
    def __init__(self, **kwargs):
        super(SalleSections, self).__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        header = BoxLayout(orientation='vertical', size_hint=(None, .1))

        quit_ = Button(
            background_normal='3.png',
            background_down='3.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': 0},
            padding=(10, 0, 10, 0)
        )
        quit_.bind(on_release=self.quit_)

        settings = Button(
            background_normal='4.png',
            background_down='4.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        settings.bind(on_press=self.settings)

        back_to_main = Button(
            background_normal='5.png',
            background_down='5.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        back_to_main.bind(on_press=self.dismiss)
        quit_.bind(on_press=self.quit_)
        header.add_widget(back_to_main)
        header.add_widget(settings)
        header.add_widget(quit_)
        self.dropdown = DropDown()
        for i in range(16):  # Numbers from 0 to 15
            btn = Button(background_normal = 'dropdown_buttons.png',text=str(i), size_hint_y=None, size = (50,50))
            btn.bind(on_release=lambda btn: self.on_dropdown_select(btn.text))
            self.dropdown.add_widget(btn)

        classroom_selector = Button(
            background_normal = 'choisir_salle_button.png',
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'x': 0, 'y': .8},
        )
        classroom_selector.bind(on_release=self.dropdown.open)
        main_layout.add_widget(classroom_selector)

        self.label = Label(text="", color=(0, 0, 0, 1)) 
        main_layout.add_widget(self.label)
        main_layout.add_widget(header)
        self.add_widget(main_layout)

#hado msalyin mayt2adawch
    def dismiss(self, instance):
        transition = SlideTransition(direction='right')
        self.manager.transition = transition
        self.manager.current = 'salle'

    def settings(self, instance):
        self.manager.current = 'settings'

    def quit_(self, instance):
        App.get_running_app().stop()

    def set_salle_section(self, salle_section):
        self.salle_section = salle_section
        return self.salle_section

    def on_enter(self):
        self.label.text = f"Selected Classroom: {self.set_salle_section(self.salle_section)}"

    def on_dropdown_select(self, value):
        self.salle_section = int(value)
        self.label.text = f"Selected Classroom: {self.set_salle_section(self.salle_section)}"
        self.dropdown.select(value)
