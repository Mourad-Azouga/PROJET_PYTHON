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
import calendar
from kivy.graphics import Rectangle, Color
from kivy.uix.textinput import TextInput


#Tabulate imports
from tabulate import tabulate

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

class room():
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
        self.reservations = {day: {} for day in emploi}
    def check_reser(self, day, timeslot):
     """Vérifie si une réservation existe à un jour et un créneau horaire donnés."""
     return (day, timeslot) in self.reservations[day]
    
    def make_reser(self, day, timeslot):
        """Designed to check if a timeslot in a day for a class is empty and adds a reserveration
        Args:
            self - to access the instance (aka the class or amphi)
            day - the day we want to make a reservation
            timeslot - the timeslot we want to be reservered (Creneau Horaire)
        Returns:
            True for success
            False for failure
        """
        if day in self.reservations and timeslot not in self.reservations[day]:
            self.reservations[day][timeslot] = "Reserved"  # Needs to be changed with the module name
            self.display_timetable()
            return True
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
            del self.reservations[day][timeslot]
            return True
        return False

    def modify_reservation(self, day, old_timeslot, new_day, new_timeslot):
        """Changes the timeslot for the reservation, calls remove to check for existance and removes the reservation
        calls for make_reservation to make the new one
        Args:
            self - to access the instance (aka the class or amphi)
            day - the day we want to make a reservation
            old_timeslot - the preexisting timeslot
            new_day - the new assigned day for the reservation
            new_timeslot - the newly created timeslot
        Returns:
            True for success
            False for failure
        """
        if self.remove_reser(day, old_timeslot):
            self.make_reser(new_day, new_timeslot)
            return True
        return False


#wa9ila anhtajo ndiro les instances kamlin hna
#Makandench ghadi nkheli materiaux (NEEDS WORK !! ATTENTION)
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

salle_E_nums = [
    room(2, {i + 1}, f"Salle E-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]

salle_F_nums = [
    room(2, {i + 1}, f"Salle F-{i + 1}", emploi, materiaux, 80)
    for i in range(15)
]
salles = [salle_A_nums, salle_B_nums, salle_E_nums, salle_F_nums]