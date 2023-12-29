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
        self.label = Label(text="", color=(0, 0, 0, 1))  # Create a label attribute
        main_layout.add_widget(self.label)

        self.layout = BoxLayout(orientation='vertical')  # Define the layout attribute

        main_layout.add_widget(header)
        main_layout.add_widget(self.layout)  # Add the layout to the main layout
        self.add_widget(main_layout)

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

    def on_enter(self):
        # Print the selected amphi number
        self.label.text = f"Selected Amphi: {self.set_amphi_number(self.amphi_number)}"

        # Define the empty timetable
        emploi = {
            'Lundi': ['', '', '', '', ''],
            'Mardi': ['', '', '', '', ''],
            'Mercredi': ['', '', '', '', ''],
            'Jeudi': ['', '', '', '', ''],
            'Vendredi': ['', '', '', '', ''],
            'Samedi': ['', '', '', '', '']
        }

        # Create a GridLayout to contain the timetable
        grid_layout = GridLayout(cols=len(emploi['Lundi']), spacing=5, size_hint_y=None)

        # Set the height of the GridLayout based on the number of rows and spacing
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Add labels for days
        for day in emploi.keys():
            grid_layout.add_widget(Label(text=day, bold=True, size_hint_y=None, height=40, color=(0, 0, 0, 1)))

        # Add labels for times and empty slots
        for day, times in emploi.items():
            for time in times:
                cell_label = Label(text=str(time), halign='left', valign='top', markup=True, size_hint_y=None, height=40, color=(0, 0, 0, 1))
                grid_layout.add_widget(cell_label)

        # Add the GridLayout to the layout
        self.layout.add_widget(grid_layout)

        # Call the parent on_enter method
        super(AmphiFinal, self).on_enter()
