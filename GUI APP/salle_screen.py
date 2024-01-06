from header import *
"""SalleScreen
    The first screen that appears after selecting the salle in the main window, in this screen the user will select the section"""
class SalleScreen(Screen):
    def __init__(self, **kwargs):
        super(SalleScreen, self).__init__(**kwargs)
        background_image = Image(source='back1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)
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
        background_image = Image(source='back1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)
        main_layout = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.salle_section_number = 0
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

        self.dropdown = DropDown(size_hint=(None, .1))
        for i in range(16):  # Numbers from 0 to 15
            btn = Button(background_normal = 'dropdown_buttons.png',background_down = 'dropdown_buttons.png',text=str(i), size_hint_y=None, size = (100,33))
            btn.bind(on_release=lambda btn: self.on_dropdown_select(btn.text))
            self.dropdown.add_widget(btn)

        classroom_selector = Button(
            background_normal = 'choisir_salle_button.png',
            background_down = 'choisir_salle_button.png',
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'x': 0, 'y': .7},
        )
        classroom_selector.bind(on_release=self.dropdown.open)
        main_layout.add_widget(classroom_selector)

        self.label = Label(text="", color=(0, 0, 0, 1),size_hint=(.3, .01), pos_hint={'x':.17, 'y':0}) 

        timetable_layout = GridLayout(cols=7, rows=6, spacing=0, size_hint=(.8, None), pos_hint={'x':.17, 'y':.30})
        timetable_layout.add_widget(Button(text="", background_color =(0,0,0,0)))

        for day in emploi.keys():
            day_button = Button(text=day, size_hint_y=None, height=90, background_normal = 'ppll.png', background_down = 'ppll.png', color = (0,0,0,1), font_size = 25)
            timetable_layout.add_widget(day_button) 

        for timeslot in emploi[list(emploi.keys())[0]]:
            time_button = Button(text=f"{timeslot[0]}\n{timeslot[1]}", size_hint_y=None, height=90, background_down = 'ppll.png', background_normal = 'ppll.png', color = (0,0,0,1), font_size = 25)
            timetable_layout.add_widget(time_button)

            for day in emploi.keys():
                cell_button = Button(text=f"Cell ({day}, {timeslot[0]})", size_hint_y=None, height=90, background_normal = 'lolo.png', color = (0,0,0,1))
                cell_button.bind(on_press=lambda instance, day=day, timeslot=timeslot[0]: self.on_click(instance, day, timeslot))
                timetable_layout.add_widget(cell_button)

        main_layout.add_widget(timetable_layout)

        self.button_layout = GridLayout(cols = 1, rows = 3, spacing = 10,size_hint = (.3,.3), pos_hint = {'x':.9, 'y':0})
        self.button_layout.add_widget(Button(
            background_normal = 'placer.png',
            background_down = 'placer.png',
            size_hint=(None, None),
            size=(150, 50),
        ))
        self.button_layout.add_widget(Button(
            background_normal = 'modifier.png',
            background_down = 'modifier.png',
            size_hint=(None, None),
            size=(150, 50),
        ))
        self.button_layout.add_widget(Button(
            background_normal = 'supprimer.png',
            background_down = 'supprimer.png',
            size_hint=(None, None),
            size=(150, 50),
        ))

        self.button_layout.opacity = 0
        self.button_layout.disabled = True 
        self.add_widget(self.button_layout)
        self.input_layout = GridLayout(cols=2, rows=5, spacing=(10, 10), size_hint=(.4, .2), pos_hint={'x': .17, 'y': 0.1})

        # Ster lwl : nom.prenom
        self.label1 = Button(background_normal = 'lolo.png',
            background_down = 'lolo.png',
            size_hint=(.2, None),
            size=(150, 30),
            text="Nom et Prenom",
            color = (0,0,0,1))
        self.input_layout.add_widget(self.label1)
        self.input_field1 = TextInput(size_hint=(.6, None), height=30, multiline=False)
        self.input_layout.add_widget(self.input_field1)

        # Ster tani: Code
        self.label2 = Button(background_normal = 'lolo.png',
            background_down = 'lolo.png',
            size_hint=(.2, None),
            size=(150, 30),
            text="Code Utilisateur",
            color = (0,0,0,1))
        self.input_layout.add_widget(self.label2)
        self.input_field2 = TextInput(size_hint=(.6, None), height=30, multiline=False)
        self.input_layout.add_widget(self.input_field2)

        # Ster talet: Profession
        self.label3 = Button(background_normal = 'lolo.png',
            background_down = 'lolo.png',
            size_hint=(.2, None),
            size=(150, 30),
            text="Profession",
            color = (0,0,0,1))
        self.input_layout.add_widget(self.label3)
        self.input_field3 = TextInput(size_hint=(.6, None), height=30, multiline=False)
        self.input_layout.add_widget(self.input_field3)

        # Ster rab3: Module
        self.label4 = Button(background_normal = 'lolo.png',
            background_down = 'lolo.png',
            size_hint=(.2, None),
            size=(150, 30),
            text="Module",
            color = (0,0,0,1))
        self.input_layout.add_widget(self.label4)
        self.input_field4 = TextInput(size_hint=(.6, None), height=30, multiline=False)
        self.input_layout.add_widget(self.input_field4)
        # Ster khames: Demandes
        self.label5 = Button(background_normal = 'ppll.png',
            background_down = 'ppll.png',
            size_hint=(.2, None),
            size=(150, 30),
            text="Demandes",
            color = (0,0,0,1))
        self.input_layout.add_widget(self.label5)
        self.input_field5 = TextInput(size_hint=(.6, None), height=30, multiline=False)
        self.input_layout.opacity = 0
        self.input_layout.disabled = True 
        self.input_layout.add_widget(self.input_field5)

        self.add_widget(self.input_layout)
        self.add_widget(main_layout)
        main_layout.add_widget(self.label)

        main_layout.add_widget(header)

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
    
    def set_salle_section_number(self, salle_section_number):
        self.salle_section_number = salle_section_number
        return self.salle_section_number

    def on_enter(self):
        self.label.text = f"Selected Classroom: {self.set_salle_section(self.salle_section)} {self.set_salle_section_number(self.salle_section_number)}"

    def on_dropdown_select(self, value):
        self.salle_section_number = int(value)
        self.label.text = f"Selected Classroom: {self.set_salle_section_number(self.salle_section_number)}"
        self.dropdown.select(value)

    def on_click(self, instance,day ,timeslot):
        self.button_layout.opacity = 1
        self.button_layout.disabled = False
        self.input_layout.opacity = 1
        self.input_layout.disabled = False
        self.label.text =  f"Selected timeslot: {day}, {timeslot} in {self.set_salle_section(self.salle_section)} at {self.set_salle_section_number(self.salle_section_number)}"
    
    def on_leave(self):
        # Hide buttons or perform actions when leaving the screen
        self.button_layout.opacity = 0
        self.button_layout.disabled = True
        self.input_layout.opacity = 0
        self.input_layout.disabled = True
        super(SalleSections, self).on_leave()