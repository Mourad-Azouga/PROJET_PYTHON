#Kivy related imports
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import SlideTransition
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.spinner import Spinner
from kivy.uix.dropdown import DropDown
from kivy.graphics import Rectangle, Color
from kivy.uix.textinput import TextInput
import ast
import re

#emploi du temps
emploi = {
    'Lundi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Mardi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Mercredi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Jeudi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Vendredi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Samedi': [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')]
}

# hna we'll store all the dictionaries and stuff, like les noms de salles w les creneaux w dakchi
# We'll make some classmethods to insert the reservation hashtable inside the room class instances
import json

class FileManager:
    '''This class will be used to parse the data from the json file'''
    @classmethod
    def parse_reservations(cls, filename):
        reservations = {}

        with open(filename, 'r') as file:
            data = json.load(file)
            for key, value in data.items():
                match = re.match(r"(.+);(.+);\((.+)\)", key)
                if match:
                    instance_name, day, timeslot_str = match.groups()
                    timeslot = tuple(ast.literal_eval(timeslot_str))
                else:
                    print(f"Invalid key format: {key}")
                    continue
                reservation_key = f"{instance_name};{day};{timeslot}"
                if reservation_key in reservations:
                    print(f"Double reservation found for {reservation_key}. Skipping.")
                    continue
                details = ast.literal_eval(value)
                if instance_name not in reservations:
                    reservations[instance_name] = {}
                if day not in reservations[instance_name]:
                    reservations[instance_name][day] = {}
                reservations[instance_name][day][timeslot] = {'details': details}

        return reservations

class room():
    instances = []
    """This is the main class of our project, it's the backbone, the beating heart
    Designed to store and navigate through all the instances(Salles and Amphis)
    This class has many methods that'll serve as the backbone of main.py methods"""

    def __init__(self, type, ID, name, emploi, materiaux, places):
        self.type = type
        self.ID = ID
        self.name = name
        self.emploi = emploi
        self.materiaux = materiaux
        self.places = places
        self.reservations = {day: {timeslot: {'details': {'Nom': None, 'Code': None, 'Profession': None, 'Module': None, 'Demandes': None}} for timeslot in emploi[day]} for day in emploi}
        self.__class__.instances.append(self)
    
    def check_reser(self, day, timeslot):
     """Vérifie si une réservation existe à un jour et un créneau horaire donnés."""
     return (day, timeslot) in self.reservations[day]
    
    def make_reser(self, day, timeslot, details):
        """Designed to check if a timeslot in a day for a class is empty and adds a reserveration
        Args:
            self - to access the instance (aka the class or amphi)
            day - the day we want to make a reservation
            timeslot - the timeslot we want to be reservered (Creneau Horaire)
        Returns:
            True for success
            False for failure
        """
        if day in self.reservations and timeslot in self.reservations[day]:
            reservation_key = f"{self.name};{day};{str(timeslot)}"
            self.reservations[day][timeslot]['details'] = details
            self.save_reservations_to_file(reservation_key, details)

            return True
        elif day not in self.reservations:
            print("The issue is the day")
        elif timeslot not in self.reservations:
            print("timeslot is the issue")
        return False

    def remove_reser(self, day, timeslot):
        """Checks for the reservation and deletes it if it exists
        Args:
            self - to access the instance (aka the class or amphi)
            day - the day we want to delete a reservation
            timeslot - the timeslot we want to be deleted (Creneau Horaire)
        Returns:
            True for success
            False for failure
        """
        if day in self.reservations and timeslot in self.reservations[day]:
            reservation_key = f"{self.name};{day};{str(timeslot)}"
            self.remove_reservation_from_file(reservation_key)
            del self.reservations[day][timeslot]
            return True
        return False
    
    def modify_reservation(self, day, timeslot, new_details=None):
        """Modifies the details of an existing reservation.
        
        Args:
            self - to access the instance (aka the class or amphi)
            day - the day of the reservation
            timeslot - the timeslot of the reservation
            new_details - the new details for the reservation (if any)
            
        Returns:
            True for success
            False for failure
        """
        if self.reservations.get(day) and self.reservations[day].get(timeslot):
            current_details = self.reservations[day][timeslot]['details']
            reservation_key = f"{self.name};{day};{str(timeslot)}"
            self.remove_reservation_from_file(reservation_key)
            if new_details:
                current_details.update(new_details)
            self.reservations[day][timeslot]['details'] = current_details
            self.save_reservations_to_file(reservation_key, current_details)
            return True
        return False
    
    @classmethod
    def load_reservations(cls, filename):
        all_reservations = FileManager.parse_reservations(filename)
        for instance_name, days in all_reservations.items():
            instance = cls.find_instance_by_name(instance_name)
            if instance:
                for day, timeslots in days.items():
                    for timeslot, details in timeslots.items():
                        # Extract the nested 'details' dictionary
                        nested_details = details.get('details', {})
                        if not instance.make_reser(day, timeslot, nested_details):
                            print(timeslot)
                            print(type(timeslot))

                            print(f"Failed to load reservation for {instance_name} on {day} at {timeslot}.")
                        else:
                            print(f"Succefully to load reservation for {instance_name} on {day} at {timeslot}.")
        return all_reservations

    @classmethod
    def find_instance_by_name(cls, name):
        for instance in cls.instances:
            if instance.name == name:
                return instance
        return None
    @classmethod
    def save_reservations_to_file(self, reservation_key, details):
        filename = 'data.json'

        with open(filename, 'r') as file:
            all_reservations = json.load(file)

        all_reservations[reservation_key] = str(details)

        with open(filename, 'w') as file:
            json.dump(all_reservations, file, indent=2)
    
    def remove_reservation_from_file(self, reservation_key):
        """Removes a reservation from the data file."""
        filename = 'data.json'

        with open(filename, 'r') as file:
            all_reservations = json.load(file)

        # Remove the reservation from the dictionary
        if reservation_key in all_reservations:
            del all_reservations[reservation_key]

            # Write the updated reservations back to the file
            with open(filename, 'w') as file:
                json.dump(all_reservations, file, indent=2)






#wa9ila anhtajo ndiro les instances kamlin hna
materiaux = "Datashow;Micro"
# 3amar les objects salles w amphis
amphi1 = room(1, 1, "Amphi1", emploi, materiaux, 115)
amphi2 = room(1, 2, "Amphi2", emploi, materiaux, 115)
amphi3 = room(1, 3, "Amphi3", emploi, materiaux, 115)
amphi4 = room(1, 4, "Amphi4", emploi, materiaux, 115)
amphi5 = room(1, 5, "Amphi5", emploi, materiaux, 300)
amphi6 = room(1, 6, "Amphi6", emploi, materiaux, 400)
amphis = [amphi1, amphi2, amphi3, amphi4, amphi5, amphi6]

salle_A_nums = [
    room(2, {i + 1}, f"Salle A-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_B_nums = [
    room(2, {i + 1}, f"Salle B-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_C_nums = [
    room(2, {i + 1}, f"Salle C-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_D_nums = [
    room(2, {i + 1}, f"Salle D-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_E_nums = [
    room(2, {i + 1}, f"Salle E-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_F_nums = [
    room(2, {i + 1}, f"Salle F-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_G_nums = [
    room(2, {i + 1}, f"Salle G-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_confi = room(2, 1, "Salle de Conférence", emploi, materiaux, 400)

salles = [salle_A_nums, salle_B_nums, salle_E_nums, salle_F_nums, salle_D_nums, salle_G_nums, salle_C_nums, salle_confi]