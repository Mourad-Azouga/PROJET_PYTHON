# hna we'll store all the dictionaries and stuff, like les noms de salles w les creneaux w dakchi
# We'll make some classmethods to insert the reservation hashtable inside the room class instances
import tabulate


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

    def modify_reservation(self, day, old_timeslot, new_timeslot):
        """Changes the timeslot for the reservation, calls remove to check for existance and removes the reservation
        calls for make_reservation to make the new one
        Args:
            self - to access the instance (aka the class or amphi)
            day - the day we want to make a reservation
            old_timeslot - the preexisting timeslot
            new_timeslot - the newly created timeslot
        Returns:
            True for success
            False for failure
        """
        if self.remove_reservation(day, old_timeslot):
            self.make_reservation(day, new_timeslot)
            return True
        return False

    def display_timetable(self):
        """Displays the timetable using tabulate, why did we make it an instance method you may ask?
        Well because it changes depending on the instance of course you dummy
        Args:
            self - to access the instance (aka the class or amphi)
        """
        headers = ["Jours"] + [f"{slot[0]} - {slot[1]}" for slot in self.emploi['Lundi']]
        table_data = [(day, *[self.reservations[day].get(slot, "") for slot in self.emploi[day]]) for day in
                      self.emploi]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))