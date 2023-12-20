from header import room
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
materiaux = "Datashow;Micro"
#3amar les objects salles w amphis
amphi1 = room(1, 1, "Amphi1", emploi, materiaux, 115)
amphi2 = room(1, 2, "Amphi2", emploi, materiaux, 115)
amphi3 = room(1, 3, "Amphi3", emploi, materiaux, 115)
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
#---------------------------------------------------------------------------------------------------------------------------------------#
#                                                           RESERVATION METHODS
#---------------------------------------------------------------------------------------------------------------------------------------#
def make_res(type, section, num):
    """Should make the reservation and add it to the system (Also to data.txt)
    Args:
        type - The type of room (1 amphi 2 class)
        section - Only applicable to classes, ranges in {A, B, E, F} the program should ignore it if it's a type = 1
        num - the number of the room
    Return:
        Nothing for now
    """

def remove_res(type, section,num):
    """Should remove the reservation from the system (Also from data.txt)
    Args:
        type - The type of room (1 amphi 2 class)
        section - Only applicable to classes, ranges in {A, B, E, F} the program should ignore it if it's a type = 1
        num - the number of the room
    Return:
        Nothing for now
    """

def modif_res(type, section, num):
    """Should modify the reservation details in the system (Also in data.txt)
    Args:
        type - The type of room (1 amphi 2 class)
        section - Only applicable to classes, ranges in {A, B, E, F} the program should ignore it if it's a type = 1
        num - the number of the room
    Return:
        Nothing for now
    """
#---------------------------------------------------------------------------------------------------------------------------------------#
#                                                          DISPLAY METHODS
#---------------------------------------------------------------------------------------------------------------------------------------#    
def display_timetable(type, section, num):
    """Displays the timetable details using tabulate and data from the data.txt file
    Args:
        type - The type of room (1 amphi 2 class)
        section - Only applicable to classes, ranges in {A, B, E, F} the program should ignore it if it's a type = 1
        num - the number of the room
    Return:
        Nothing for now
    """

    #NB - Not done yet
    first_day_slots = emploi['Lundi']
    timetable = {day: [""] * len(first_day_slots) for day in emploi}
    headers = ["Jours"] + [f"{slot}" for slot in first_day_slots]
    table_data = [(day, *slots) for day, slots in timetable.items()]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


#---------------------------------------------------------------------------------------------------------------------------------------#
#                                                          NAVIGATION METHODS
#---------------------------------------------------------------------------------------------------------------------------------------# 
    
def navigator_amphi():
    """The first base for the amphis, where we'll have the menu"""

    type = 1
    amphi_numero = int(input("Vous avez choisis les amphis!\nSVP de choisir le numero d'amphi (1 - 6): "))
    if amphi_numero < 1 or amphi_numero > 6:
        print("Erreur de saisie!")
        return 
    print("Vous avez choisi amphi {}\nL'emploi du temps present de cet amphi:\n".format(amphi_numero))
    display_timetable(type, 0, amphi_numero)
    choix = int(input("Menu:\n_______________\n(1) Faire une reservation\n(2) Annule une reservation\n(3) Modifier une reservation \n(4) Retour au menu principal\n"))
    match (choix):
        case 1:
            make_res(type, 0, amphi_numero)
        case 2:
            remove_res(type, 0, amphi_numero)
        case 3:
            modif_res(type, 0, amphi_numero)
        case 4:
            print("Retour..\n")
            return
        case _:
            print("Erreur saisir!\n")
            return

def navigator_salles():
    """The first base for the salles, where we'll have the menu, it should also test the input before doing anything"""

    type = 2
    salle_section = input("Vous avez choisis les salles!\nSVP de choisir le section du salle (A-B-E-F)\n")
    if salle_section not in {'A', 'B', 'E', 'F'}:
        print("Erreur saisie!\n")
        return
    salle_numero = int(input("Vous avez choisi les salles de section {}, SVP de choisir le numero de salle: ".format(salle_section)))
    if salle_numero < 1 or salle_numero > 15:
        print("Erreur de saisie!")
        return 
    print("Vous avez choisi la salle {}{}\nL'emploi du temps present de cet amphi:\n".format(salle_section, salle_numero))

    display_timetable(type, salle_section, salle_numero)
    choix = int(input("Menu:\n_______________\n(1) Faire une reservation\n(2) Annule une reservation\n(3) Modifier une reservation \n(4) Retour au menu principal\n"))
    match (choix):
        case 1:
            make_res(type, salle_section, salle_numero)
        case 2:
            remove_res(type, salle_section, salle_numero)
        case 3:
            modif_res(type, salle_section, salle_numero)
        case 4:
            print("Retour..\n")
            return
        case _:
            print("Erreur saisir!\n")
            return


if __name__ == '__main__':
    print("Bienvenu au system gestion TIMEXI\n")
    while True:
        choix = int(input("\nMenu Principal\n_______________\n(1)Les Amphis\n(2)Les Salles\n(3)To be made\n(4)Quitter\n"))
        match choix:
            case 1:
                navigator_amphi()
            case 2:
                navigator_salles()
            case 3:
                print("")
            case 4:
                print("Au revoir")
                break