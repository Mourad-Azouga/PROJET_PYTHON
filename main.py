from data import room
from tabulate import tabulate


#initalize les jours w les creneaux
emploi = {
    'Lundi' : [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Mardi' : [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Mercredi' : [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Jeudi' : [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Vendredi' : [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')],
    'Samedi' : [('9:00 AM', '10:45 AM'), ('11:00 AM', '12:45 PM'), ('1:00 PM', '2:45 PM'), ('3:00 PM', '4:45 PM'), ('5:00 PM', '6:45 PM')]
}
materiaux = "Datashow"
#3amar les objects salles w amphis
amphi1 = room(1, 1, "Amphi1", emploi, materiaux, 115)
amphi2 = room(1, 2, "Amphi2", emploi, materiaux, 115)
amphi3 = room(1, 3, "Amphi3", emploi, materiaux, 115)
#WOWOWOWWOWOOW
amphi4 = room(1, 4, "Amphi4", emploi, materiaux, 115)
amphi5 = room(1, 5, "Amphi5", emploi, materiaux, 300)
amphi6 = room(1, 6, "Amphi6", emploi, materiaux, 400)
amphis = [amphi1, amphi2, amphi3, amphi4, amphi5, amphi6]

salle_A_nums = [
    room(2, {i+1}, f"Salle A-{i+1}", emploi, materiaux, 80) 
    for i in range(15)
    ]

salle_B_nums = [
    room(2, {i+1}, f"Salle B-{i+1}", emploi, materiaux, 80) 
    for i in range(15)
    ]

salle_E_nums = [
    room(2, {i+1}, f"Salle E-{i+1}", emploi, materiaux, 80) 
    for i in range(15)
    ]

salle_F_nums = [
    room(2, {i+1}, f"Salle F-{i+1}", emploi, materiaux, 80) 
    for i in range(15)
    ]
salles = [salle_A_nums, salle_B_nums, salle_E_nums, salle_F_nums]
#Tres bien! Maintenant qu'on a deja initialiser tous nos salles et amphis aussi que l'emploi du temps
#On doit faire les methods pours faire les choses
#Commencons par l'user interface (Avant de faire kivy GUI)
def create_and_display_timetable():
    # Extracting time slots from the first day (assuming the same slots for each day)
    first_day_slots = emploi['Lundi']
    
    # Creating a timetable structure
    timetable = {day: ["3amar"] * len(first_day_slots) for day in emploi}

    # Displaying the timetable using tabulate
    headers = ["Jours"] + [f"{slot}" for slot in first_day_slots]
    table_data = [(day, *slots) for day, slots in timetable.items()]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

if __name__ == '__main__':
    print("Bienvenu au system gestion TIMEXI\n")
    while True:
        print("\nList d'operations:\nTaper 1 pour: Les Amphis\nTaper 2 pour: Les Salles\nTaper 3 pour: (To be made)\nTaper 4 pour: Sortir\n")
        choix = int(input(""))
        match choix:
            case 1:
                print("Ghadi ndahro wahd la liste dial les amphis, moraha ghadi ikhtar wahd l'amphi ")
            case 2:
                print("Les Salles")
            case 3:
                print("")
            case 4:
                create_and_display_timetable()
                