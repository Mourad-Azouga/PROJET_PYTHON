from header import *
class ConfiScreen(Screen):
    def __init__(self, **kwargs):
        super(ConfiScreen, self).__init__(**kwargs)
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

        self.label = Label(text="", color=(0, 0, 0, 1),size_hint=(.3, .01), pos_hint={'x':.7, 'y':0.01}, font_size = 24) 

        timetable_layout = GridLayout(cols=7, rows=6, spacing=1, size_hint=(.8, None), pos_hint={'x':.17, 'y':.30})
        timetable_layout.add_widget(Button(text="", background_color =(0,0,0,0)))
        self.cell_buttons = {}
        for day in emploi.keys():
            day_button = Button(text=day, size_hint_y=None, height=90, background_normal = 'ppll.png', background_down = 'ppll.png', color = (0,0,0,1), font_size = 25)
            timetable_layout.add_widget(day_button) 

        for timeslot in emploi[list(emploi.keys())[0]]:
            time_button = Button(text=f"{timeslot[0]}\n{timeslot[1]}", size_hint_y=None, height=90, background_down = 'ppll.png', background_normal = 'ppll.png', color = (0,0,0,1), font_size = 25)
            timetable_layout.add_widget(time_button)

            for day in emploi.keys():
                
                cell_button = Button(text="", size_hint_y=None, height=90, background_normal = 'lolo.png', color = (0,0,0,1))
                cell_button.bind(on_press=lambda instance, day=day, timeslot=timeslot: self.on_click(instance, day, timeslot))
                timetable_layout.add_widget(cell_button)
                self.cell_buttons[(day, timeslot)] = cell_button

        main_layout.add_widget(timetable_layout)

        self.button_layout = GridLayout(cols = 1, rows = 3, spacing = 10,size_hint = (.3,.3), pos_hint = {'x':.9, 'y':0})
        placer_res = Button(
            background_normal = 'placer.png',
            background_down = 'placer.png',
            size_hint=(None, None),
            size=(150, 50),
        )
        self.button_layout.add_widget(placer_res)
        placer_res.bind(on_press=self.place_reservation)

        modif_res = Button(
            background_normal = 'modifier.png',
            background_down = 'modifier.png',
            size_hint=(None, None),
            size=(150, 50),
        )
        self.button_layout.add_widget(modif_res)
        modif_res.bind(on_press= self.modify_reservation)

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
        self.add_widget(self.label)
        main_layout.add_widget(header)

#hado msalyin mayt2adawch
    def dismiss(self, instance):
        transition = SlideTransition(direction='right')
        self.manager.transition = transition
        self.manager.current = 'main'

    def settings(self, instance):
        self.manager.current = 'settings'

    def quit_(self, instance):
        App.get_running_app().stop()

    def on_enter(self):
        self.label.text = f"Selected Classroom: Salle de Conférence"
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

    def find_room_instance(self, selected_salle_name):
        for room_instance in salles:
            if room_instance == salle_confi:
                return room_instance
        return None
    
    def update_cell_button_texts(self, selected_room):
        for (day, timeslot), cell_button in self.cell_buttons.items():
            reservation_details = selected_room.reservations.get(day, {}).get(timeslot, {}).get('details', {})
            print(f"Day: {day}, Timeslot: {timeslot}, Reservation Details: {reservation_details}")
            module_name = reservation_details.get('Module', '')
            print(f"Module Name: {module_name}")
            # Set the button text based on the reservation details
            if module_name == None:
                cell_button.text = ""
            else:
                cell_button.text = f"{module_name}"

    def on_click(self, instance, day ,timeslot):
        self.button_layout.opacity = 1
        self.button_layout.disabled = False
        self.input_layout.opacity = 1
        self.input_layout.disabled = False
        self.label.text =  f"Selected timeslot: {day}, {timeslot} in Salle de Conférence"
        self.current_day = day
        self.current_timeslot = timeslot

        selected_salle_name = f"Salle de Conférence"
        selected_room = self.find_room_instance(selected_salle_name)
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

    def modify_reservation(self, instance):
        selected_salle_name = f"Salle de Conférence"
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
        selected_salle_name = f"Salle de Conférence"
        selected_room = self.find_room_instance(selected_salle_name)

        if selected_room and self.current_day and self.current_timeslot:
            nom_prenom = self.input_field1.text
            code_utilisateur = self.input_field2.text
            profession = self.input_field3.text
            module = self.input_field4.text
            demandes = self.input_field5.text

            details = {"Nom": nom_prenom, "Code": code_utilisateur, "Profession": profession, "Module": module, "Demandes": demandes}
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
        selected_salle_name = f"Salle de Conférence"
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

    def on_leave(self):
        # Hide buttons or perform actions when leaving the screen
        self.button_layout.opacity = 0
        self.button_layout.disabled = True
        self.input_layout.opacity = 0
        self.input_layout.disabled = True
        super(ConfiScreen, self).on_leave()