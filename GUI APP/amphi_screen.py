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
        ster_1 = BoxLayout(
            orientation='horizontal',
            padding=(30, 0, 0, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint = {'x': 0.1, 'y': 1}
        )

        amphi1 = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        amphi1.bind(on_press=lambda instance: self.amphi_button_press(instance, 1))

        amphi2 = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        amphi2.bind(on_press=lambda instance: self.amphi_button_press(instance, 2))

        #ghadi n addiw les buttons n ster lwlani
        ster_1.add_widget(amphi1)


        ster_1.add_widget(amphi2)
        main_layout.add_widget(ster_1)

        ster_2 = BoxLayout(
            orientation='horizontal',
            padding=(30, 0, 0, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint = {'x': 0.1, 'y': 0}
        )

        amphi3 = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint =(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        amphi3.bind(on_press=lambda instance: self.amphi_button_press(instance, 3))


        amphi4 = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        amphi4.bind(on_press=lambda instance: self.amphi_button_press(instance, 4))

        ster_2.add_widget(amphi3)
        ster_2.add_widget(amphi4)
        main_layout.add_widget(ster_2)


        ster_3 = BoxLayout(
            orientation='horizontal',
            padding=(30, 0, 0, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint = {'x': 0.1, 'y': 0}
        )

        amphi5 = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint =(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        amphi5.bind(on_press=lambda instance: self.amphi_button_press(instance, 5))


        amphi6 = Button(
            background_normal='1.png',
            background_down='1.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        amphi6.bind(on_press=lambda instance: self.amphi_button_press(instance, 6))

        ster_3.add_widget(amphi5)
        ster_3.add_widget(amphi6)

        main_layout.add_widget(ster_3)
        main_layout.add_widget(header)






        self.add_widget(main_layout)
    """
    Series of methods to be linked with the amphi buttons
    Each method needs to send the number of the amphi to the amphi_final
    so that we can know what number amphi the user wants to operate on without
    making each amphi a file with their personal screen (not implemented correctly yet)
    """
    def amphi_button_press(self, instance, amphi_num):
        # Set amphi_number in AmphiFinal and transition to it
        amphi_number = amphi_num
        amphi_final_screen = self.manager.get_screen('amphi_final')
        amphi_final_screen.set_amphi_number(amphi_number)
        transition = SlideTransition(direction='left')
        self.manager.transition = transition
        self.manager.current = 'amphi_final'


#Hado dok les trois buttons safi msalyin don't touch
    def dismiss(self, instance):
        transition = SlideTransition(direction='right')
        self.manager.transition = transition
        self.manager.current = 'main'

    def settings(self, instance):
        self.manager.current = 'settings'

    def quit_(self, instance):
        App.get_running_app().stop()
    
class AmphiFinal(Screen):
    def __init__(self, **kwargs):
        super(AmphiFinal, self).__init__(**kwargs)
        self.set_amphi_number(0)
        self.amphi_number = 0

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

        self.label = Label(text="", color=(0, 0, 0, 1),size_hint=(.2, .2))
        main_layout.add_widget(self.label)
        self.calendar = Label(text="", color=(0, 0, 0, 1), pos_hint={'x':0, 'y':.6}, size_hint= (.2,.2), font_size = 25)
        self.add_widget(self.calendar)

        timetable_layout = GridLayout(cols=7, rows=6, spacing=0, size_hint=(.8, None), pos_hint={'x':.17, 'y':.15})
        timetable_layout.add_widget(Button(text=""))

        for day in emploi.keys():
            day_button = Button(text=day, size_hint_y=None, height=90)
            timetable_layout.add_widget(day_button)

        for timeslot in emploi[list(emploi.keys())[0]]:
            time_button = Button(text=f"{timeslot[0]} - {timeslot[1]}", size_hint_y=None, height=90)
            timetable_layout.add_widget(time_button)

            # Populate the rest of the row with cell buttons
            for day in emploi.keys():
                cell_button = Button(text=f"Cell ({day}, {timeslot[0]})", size_hint_y=None, height=90, background_color=(0, 0, 0, 0.1), background_down = '1.png', color = (0,0,0,1))
                cell_button.bind(on_press=lambda instance, day=day, timeslot=timeslot[0]: self.on_click(instance, day, timeslot))
                timetable_layout.add_widget(cell_button)

        main_layout.add_widget(timetable_layout)

        self.layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.layout)

        self.label2 = Label(text="", color=(0, 0, 0, 1))
        main_layout.add_widget(self.label2)

        self.button_layout = GridLayout(cols = 1, rows = 3, spacing = 10, size_hint = (.1, .6), pos_hint = {'x':.85, 'y':.2})
        self.button_layout.add_widget(Button(text = 'Placer reservation'))
        self.button_layout.add_widget(Button(text = 'Modifier reservation'))
        self.button_layout.add_widget(Button(text = 'Annuler reservation'))
        self.button_layout.opacity = 0
        self.button_layout.disabled = True 
        main_layout.add_widget(self.button_layout)

        self.add_widget(main_layout)
        main_layout.add_widget(header)


    def dismiss(self, instance):
        transition = SlideTransition(direction='right')
        self.manager.transition = transition
        self.manager.current = 'amphi'

    def settings(self, instance):
        self.manager.current = 'settings'

    def quit_(self, instance):
        App.get_running_app().stop()

    def set_amphi_number(self, amphi_number):
        self.amphi_number = amphi_number
        return self.amphi_number
    
    def on_click(self, instance,day ,timeslot):
        self.button_layout.opacity = 1
        self.button_layout.disabled = False
        self.label2.text = f"Selected timeslot: {day}, {timeslot}"
    
  

    def on_enter(self):
        self.label.text = f"Selected Amphi: {self.set_amphi_number(self.amphi_number)}"
        cal = calendar.TextCalendar()
        self.calendar.text = cal.formatmonth(2024, 1)
        super(AmphiFinal, self).on_enter()


