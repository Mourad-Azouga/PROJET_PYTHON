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
        header.add_widget(quit_)

#All the buttons
        #First line: Button A + B
        main_buttons_1 = BoxLayout(
            orientation='horizontal',
            padding=(30, 30, 30, 30),
            spacing=30,
            size_hint=(.7, .8), pos_hint={'x': 0.15, 'y': 0}
        )

        SALLE_A = Button(
            background_normal='empty_salle.png',
            background_down='empty_salle.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "SALLE A",
            color = (0,0,0,1),
            font_size = 70
        )
        SALLE_A.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle A'))

        SALLE_B = Button(
            background_normal='empty_salle.png',
            background_down='empty_salle.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "SALLE B",
            color = (0,0,0,1),
            font_size = 70
        )
        SALLE_B.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle B'))

        main_buttons_1.add_widget(SALLE_A)
        main_buttons_1.add_widget(SALLE_B)
        main_layout.add_widget(main_buttons_1)

        #Line 2: button E + F
        main_buttons_2 = BoxLayout(
            orientation='horizontal',
            padding=(30, 30, 30, 30),
            spacing=30,
            size_hint=(.7, .8), pos_hint={'x': 0.15, 'y': 0}
        )

        SALLE_C = Button(
            background_normal='empty_salle.png',
            background_down='empty_salle.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "SALLE C",
            color = (0,0,0,1),
            font_size = 70
        )
        SALLE_C.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle C'))

        SALLE_D = Button(
            background_normal='empty_salle.png',
            background_down='empty_salle.png',
            size=(600, 300),
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "SALLE D",
            color = (0,0,0,1),
            font_size = 70
        )
        SALLE_D.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle D'))

        main_buttons_2.add_widget(SALLE_C)
        main_buttons_2.add_widget(SALLE_D)
        main_layout.add_widget(main_buttons_2)

        #Line3 G + D
        main_buttons_3 = BoxLayout(
            orientation='horizontal',
            padding=(30, 30, 30, 30),
            spacing=30,
            size_hint=(.7, .8), pos_hint={'x': 0.15, 'y': 0}
        )

        SALLE_E = Button(
            background_normal='empty_salle.png',
            background_down='empty_salle.png',
            size=(600, 300),
            size_hint=(.5, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "SALLE E",
            color = (0,0,0,1),
            font_size = 70
        )
        SALLE_E.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle E'))

        SALLE_F = Button(
            background_normal='empty_salle.png',
            background_down='empty_salle.png',
            size=(600, 300),
            size_hint=(.5, 1),
            pos_hint={'x': 0, 'y': 0},
            text = "SALLE F",
            color = (0,0,0,1),
            font_size = 70
        )
        SALLE_F.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle F'))

        main_buttons_3.add_widget(SALLE_E)
        main_buttons_3.add_widget(SALLE_F)
        main_layout.add_widget(main_buttons_3)


        #line 4: fih salle C
        main_buttons_4 = BoxLayout(
            orientation='horizontal',
            padding=(30, 30, 30, 30),
            spacing=30,
            size_hint=(.8, .8), pos_hint={'x': 0.32, 'y': 0}
        )

        SALLE_G = Button(
            background_normal='empty_salle.png',
            background_down='empty_salle.png',
            size=(600, 300),
            size_hint_x=None,
            pos_hint={'x': 0, 'y': 0},
            text = "SALLE G",
            color = (0,0,0,1),
            font_size = 70
        )
        SALLE_G.bind(on_press=lambda instance: self.salle_button_press(instance, 'Salle G'))
        main_buttons_4.add_widget(SALLE_G)

        main_layout.add_widget(main_buttons_4)
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
                
                cell_button = Button(text="", size_hint_y=None, height=90, background_normal = 'lolo.png', color = (0,0,0,1), font_size = 25)
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
        self.manager.current = 'salle'

    def quit_(self, instance):
        App.get_running_app().stop()
    
    def screenshot(self, instance):
        screenshot_filename = f"{self.name}.png"
        Window.screenshot(name=screenshot_filename)
        print(f'Screenshot saved as {screenshot_filename}')

    def set_salle_section(self, salle_section):
        self.salle_section = salle_section
        return self.salle_section
    
    def set_salle_section_number(self, salle_section_number):
        self.salle_section_number = salle_section_number
        return self.salle_section_number

    def on_enter(self):
        self.label.text = f"Selected Classroom: {self.set_salle_section(self.salle_section)} {self.set_salle_section_number(self.salle_section_number)}"
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
        for room_list in salles:
            for room_instance in room_list:
                if room_instance.name == selected_salle_name:
                    return room_instance
        return None
    
    def update_cell_button_texts(self, selected_room):
        for (day, timeslot), cell_button in self.cell_buttons.items():
            reservation_details = selected_room.reservations.get(day, {}).get(timeslot, {}).get('details', {})
            prof_name = reservation_details.get('Nom', '')
            module_name = reservation_details.get('Module', '')
            if module_name == None:
                cell_button.text = ""
            else:
                cell_button.text = f"{module_name}\n{prof_name}"

    def on_dropdown_select(self, value):
        self.salle_section_number = int(value)
        selected_salle_name = f"{self.set_salle_section(self.salle_section)}-{self.set_salle_section_number(self.salle_section_number)}"
        selected_room = self.find_room_instance(selected_salle_name)

        if selected_room:
            self.label.text = f"Selected Classroom: {selected_room.name}, Capacity: {selected_room.places}"
            self.update_cell_button_texts(selected_room)
        else:
            self.label.text = "Selected Classroom not found"  
        
        self.dropdown.select(value)

    def on_click(self, instance,day ,timeslot):
        if self.salle_section is None or self.salle_section_number == 0 or self.salle_section_number is None:
            return
        self.button_layout.opacity = 1
        self.button_layout.disabled = False
        self.input_layout.opacity = 1
        self.input_layout.disabled = False
        self.label.text =  f"Selected timeslot: {day}, {timeslot} in {self.set_salle_section(self.salle_section)} at {self.set_salle_section_number(self.salle_section_number)}"
        self.current_day = day
        self.current_timeslot = timeslot

        selected_salle_name = f"{self.set_salle_section(self.salle_section)}-{self.set_salle_section_number(self.salle_section_number)}"
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
        selected_salle_name = f"{self.set_salle_section(self.salle_section)}-{self.set_salle_section_number(self.salle_section_number)}"
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
        selected_salle_name = f"{self.set_salle_section(self.salle_section)}-{self.set_salle_section_number(self.salle_section_number)}"
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
        selected_salle_name = f"{self.set_salle_section(self.salle_section)}-{self.set_salle_section_number(self.salle_section_number)}"
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
        super(SalleSections, self).on_leave()