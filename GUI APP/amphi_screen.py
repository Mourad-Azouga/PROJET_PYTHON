# File: Amphi_screen.py
from header import *
from kivy.app import App

class AmphiScreen(Screen):
    def __init__(self, **kwargs):
        super(AmphiScreen, self).__init__(**kwargs)
        background_image = Image(source='back1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)
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
        header.add_widget(quit_)

        #hna kanbdaw b les buttons
        ster_1 = BoxLayout(
            orientation='horizontal',
            padding=(30, 0, 0, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint = {'x': 0.1, 'y': 1}
        )

        amphi1 = Button(
            background_normal='empty_amphi.png',
            background_down='empty_amphi.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "AMPHI 1",
            color = (0,0,0,1),
            font_size = 80
        )
        amphi1.bind(on_press=lambda instance: self.amphi_button_press(instance, 1))

        amphi2 = Button(
             background_normal='empty_amphi.png',
            background_down='empty_amphi.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "AMPHI 2",
            color = (0,0,0,1),
            font_size = 80
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
            background_normal='empty_amphi.png',
            background_down='empty_amphi.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "AMPHI 3",
            color = (0,0,0,1),
            font_size = 80
        )
        amphi3.bind(on_press=lambda instance: self.amphi_button_press(instance, 3))


        amphi4 = Button(
            background_normal='empty_amphi.png',
            background_down='empty_amphi.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "AMPHI 4",
            color = (0,0,0,1),
            font_size = 80
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
            background_normal='empty_amphi.png',
            background_down='empty_amphi.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "AMPHI 5",
            color = (0,0,0,1),
            font_size = 80
        )
        amphi5.bind(on_press=lambda instance: self.amphi_button_press(instance, 5))


        amphi6 = Button(
            background_normal='empty_amphi.png',
            background_down='empty_amphi.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "AMPHI 6",
            color = (0,0,0,1),
            font_size = 80
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

    def quit_(self, instance):
        App.get_running_app().stop()
    
class AmphiFinal(Screen):
    def __init__(self, **kwargs):

        super(AmphiFinal, self).__init__(**kwargs)
        background_image = Image(source='back1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)
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

        back_to_main = Button(
            background_normal='5.png',
            background_down='5.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        back_to_main.bind(on_press=self.dismiss)
        screenshot = Button(
            background_normal='4.png',
            background_down='4.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        screenshot.bind(on_press=self.screenshot)
        quit_.bind(on_press=self.quit_)
        header.add_widget(screenshot)
        header.add_widget(back_to_main)
        header.add_widget(quit_)
        #hadi gher bach nhabt timetable b .1
        self.pusher = Label(text="", color=(0, 0, 0, 1),size_hint=(.2, .1))
        main_layout.add_widget(self.pusher)
  
  

        timetable_layout = GridLayout(cols=7, rows=6, spacing=5, size_hint=(.8, None), pos_hint={'x':.17, 'y':1})
        timetable_layout.add_widget(Button(text="", background_color = (0,0,0,0)))
        self.cell_buttons = {}

        for day in emploi.keys():
            day_button = Button(text=day, size_hint_y=None, height=90, background_down = 'ppll.png', background_normal = 'ppll.png', color = (0,0,0,1), font_size = 25)
            timetable_layout.add_widget(day_button)

        for timeslot in emploi[list(emploi.keys())[0]]:
            time_button = Button(text=f"{timeslot[0]}\n{timeslot[1]}", size_hint_y=None, height=90, background_down = 'ppll.png', background_normal = 'ppll.png', color = (0,0,0,1), font_size = 25)
            timetable_layout.add_widget(time_button)

            # Populate the rest of the row with cell buttons
            for day in emploi.keys():
                cell_button = Button(text=f"", size_hint_y=None, height=90, background_normal = 'lolo.png', background_down = 'lolo.png', color = (0,0,0,1), font_size = 25)
                cell_button.bind(on_press=lambda instance, day=day, timeslot=timeslot: self.on_click(instance, day, timeslot))
                timetable_layout.add_widget(cell_button)
                self.cell_buttons[(day, timeslot)] = cell_button


        main_layout.add_widget(timetable_layout)

        self.layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.layout)


        
        self.button_layout = GridLayout(cols = 1, rows = 3, spacing = 10,size_hint = (.1,.2), pos_hint = {'x':.9, 'y':0.1})
        placer_res = Button(
            background_normal = 'placer.png',
            background_down = 'placer.png',
            size_hint=(None, None),
            size=(150, 50),
        )
        self.button_layout.add_widget(placer_res)
        placer_res.bind(on_press=self.place_reservation)

        modifi_res = Button(
            background_normal = 'modifier.png',
            background_down = 'modifier.png',
            size_hint=(None, None),
            size=(150, 50),
        )
        self.button_layout.add_widget(modifi_res)
        modifi_res.bind(on_press= self.modify_reservation)

        suppi_res = Button(
            background_normal = 'supprimer.png',
            background_down = 'supprimer.png',
            size_hint=(None, None),
            size=(150, 50),
        )
        self.button_layout.add_widget(suppi_res)
        suppi_res.bind(on_press= self.cancel_reservation)

        self.button_layout.opacity = 0
        self.button_layout.disabled = True 
        self.add_widget(self.button_layout)
        self.label = Label(text="", color=(0, 0, 0, 1),size_hint=(.3, .01), pos_hint={'x':.7, 'y':0.01}, font_size = 24) 
        self.add_widget(self.label)
        self.input_layout = GridLayout(cols=3, rows=5, spacing=(10, 10), size_hint=(.5, .2), pos_hint={'x': .17, 'y': 0.1})

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
        self.output_label1 = Label(text="",size_hint=(.6, None), height=30, color = (0,0,0,1))
        self.input_layout.add_widget(self.output_label1)

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
        self.output_label2 = Label(text="",size_hint=(.6, None), height=30, color = (0,0,0,1))
        self.input_layout.add_widget(self.output_label2)

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
        self.output_label3 = Label(text="",size_hint=(.6, None), height=30, color = (0,0,0,1))
        self.input_layout.add_widget(self.output_label3)

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
        self.output_label4 = Label(text="",size_hint=(.6, None), height=30, color = (0,0,0,1))
        self.input_layout.add_widget(self.output_label4)

        # Ster khames: Demandes
        self.label5 = Button(background_normal = 'lolo.png',
            background_down = 'lolo.png',
            size_hint=(.2, None),
            size=(150, 30),
            text="Demandes",
            color = (0,0,0,1))
        self.input_layout.add_widget(self.label5)
        self.input_field5 = TextInput(size_hint=(.6, None), height=30, multiline=False)
        self.input_layout.opacity = 0
        self.input_layout.disabled = True 
        self.input_layout.add_widget(self.input_field5)
        self.output_label5 = Label(text="",size_hint=(.6, None), height=30, color = (0,0,0,1))
        self.input_layout.add_widget(self.output_label5)

        self.add_widget(self.input_layout)

        self.add_widget(main_layout)
        main_layout.add_widget(header)



    def dismiss(self, instance):
        transition = SlideTransition(direction='right')
        self.manager.transition = transition
        self.manager.current = 'amphi'

    def quit_(self, instance):
        App.get_running_app().stop()

    def screenshot(self, instance):
        screenshot_filename = f"{self.name}.png"
        Window.screenshot(name=screenshot_filename)
        print(f'Screenshot saved as {screenshot_filename}')

    def set_amphi_number(self, amphi_number):
        self.amphi_number = amphi_number
        return self.amphi_number
    
    def on_click(self, instance, day, timeslot):
        self.button_layout.opacity = 1
        self.button_layout.disabled = False
        self.input_layout.opacity = 1
        self.input_layout.disabled = False
        self.label.text = f"Selected timeslot: {day}, {timeslot} on {self.set_amphi_number(self.amphi_number)}"
        self.current_day = day
        self.current_timeslot = timeslot

        # Check if the timeslot is already reserved
        selected_room = self.find_room_instance(f"Amphi{self.set_amphi_number(self.amphi_number)}")
        if day in selected_room.reservations and timeslot in selected_room.reservations[day]:
            # If reserved, fill labels with reservation details
            reservation_details = selected_room.reservations[day][timeslot]['details']
            
            # Check if reservation details are available
            if reservation_details:
                self.output_label1.text = f"{reservation_details['Nom']}"
                self.output_label2.text = f"{reservation_details['Code']}"
                self.output_label3.text = f"{reservation_details['Profession']}"
                self.output_label4.text = f"{reservation_details['Module']}"
                self.output_label5.text = f"{reservation_details['Demandes']}"
        if self.output_label1.text == "None":
            self.output_label1.text = ""
        if self.output_label2.text == "None":
            self.output_label2.text = ""
        if self.output_label3.text == "None":
            self.output_label3.text = ""
        if self.output_label4.text == "None":
            self.output_label4.text = ""
        if self.output_label5.text == "None":
            self.output_label5.text = ""



    
    def update_cell_button_texts(self, selected_room):
        for (day, timeslot), cell_button in self.cell_buttons.items():
            reservation_details = selected_room.reservations.get(day, {}).get(timeslot, {}).get('details', {})
            module_name = reservation_details.get('Module', '')
            prof_name = reservation_details.get('Nom', '')
            # Set the button text based on the reservation details
            if module_name == None:
                cell_button.text = ""
            else:
                cell_button.text = f"{module_name}\n{prof_name}"



    def find_room_instance(self, selected_salle_name):
        for room_instance in amphis:
            if room_instance.name == selected_salle_name:
                return room_instance
        return None    
    
    def modify_reservation(self, instance):
        selected_salle_name = f"Amphi{self.set_amphi_number(self.amphi_number)}"
        selected_room = self.find_room_instance(selected_salle_name)

        if selected_room and self.current_day and self.current_timeslot:
            nom_prenom = self.input_field1.text
            code_utilisateur = self.input_field2.text
            profession = self.input_field3.text
            module = self.input_field4.text
            demandes = self.input_field5.text

            new_details = {"Nom": nom_prenom, "Code": code_utilisateur, "Profession": profession, "Module": module, "Demandes": demandes}
            # Retrieve current details
            current_details = selected_room.reservations[self.current_day][self.current_timeslot]['details']

            # Create a new dictionary with merged details
            updated_details = {
                key: new_details[key] if new_details[key] != "" else current_details[key] for key in current_details
            }

            success = selected_room.modify_reservation(self.current_day, self.current_timeslot, new_details=updated_details)

            if success:
                self.label.text = f"Reservation modified for {self.current_day}, {self.current_timeslot} in {selected_room.name}"
                self.update_cell_button_texts(selected_room)
                self.input_field1.text = ""
                self.input_field2.text = ""
                self.input_field3.text = ""
                self.input_field4.text = ""
                self.input_field5.text = ""
            else:
                self.label.text = f"Reservation modification failed for {self.current_day}, {self.current_timeslot}"
        else:
            self.label.text = "Error modifying reservation"

    def place_reservation(self, instance):
        selected_salle_name = f"Amphi{self.set_amphi_number(self.amphi_number)}"
        selected_room = self.find_room_instance(selected_salle_name)

        if selected_room and self.current_day and self.current_timeslot:
            nom_prenom = self.input_field1.text
            code_utilisateur = self.input_field2.text
            profession = self.input_field3.text
            module = self.input_field4.text
            demandes = self.input_field5.text

            details = {"Nom": nom_prenom, "Code": code_utilisateur, "Profession": profession, "Module": module, "Demandes": demandes}
            print(self.current_timeslot)
            print(type(self.current_timeslot))

            success = selected_room.make_reser(self.current_day, self.current_timeslot, details=details)
            if success:
                self.label.text = f"Reservation placed for {self.current_day}, {self.current_timeslot} in {selected_room.name}"
                self.update_cell_button_texts(selected_room)
                self.input_field1.text = ""
                self.input_field2.text = ""
                self.input_field3.text = ""
                self.input_field4.text = ""
                self.input_field5.text = ""
            else:
                self.label.text = f"Reservation failed for {self.current_day}, {self.current_timeslot}"
        else:
            self.label.text = "Error placing reservation"

    def cancel_reservation(self, instance):
        selected_salle_name = f"Amphi{self.set_amphi_number(self.amphi_number)}"
        selected_room = self.find_room_instance(selected_salle_name)

        if selected_room and self.current_day and self.current_timeslot:
            success = selected_room.remove_reser(self.current_day, self.current_timeslot)

            if success:
                self.label.text = f"Reservation canceled for {self.current_day}, {self.current_timeslot} in {selected_room.name}"
                self.update_cell_button_texts(selected_room)
            else:
                self.label.text = f"Reservation cancellation failed for {self.current_day}, {self.current_timeslot}"
        else:
            self.label.text = "Error canceling reservation"

    def on_enter(self):
        selected_salle_name = f"Amphi{self.set_amphi_number(self.amphi_number)}"
        selected_room = self.find_room_instance(selected_salle_name)
        self.label.text = f"Selected Amphi: {self.set_amphi_number(self.amphi_number)}"
        self.update_cell_button_texts(selected_room)
        

        if self.output_label1.text == "None":
                self.output_label1.text = ""
        if self.output_label2.text == "None":
            self.output_label2.text = ""
        if self.output_label3.text == "None":
            self.output_label3.text = ""
        if self.output_label4.text == "None":
            self.output_label4.text = ""
        if self.output_label5.text == "None":
            self.output_label5.text = ""
        super(AmphiFinal, self).on_enter()

    def on_leave(self):
        # Hide buttons or perform actions when leaving the screen
        self.button_layout.opacity = 0
        self.button_layout.disabled = True
        self.input_layout.opacity = 0
        self.input_layout.disabled = True
        super(AmphiFinal, self).on_leave()
        