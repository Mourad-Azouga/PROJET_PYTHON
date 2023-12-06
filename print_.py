from main import emploi
from tabulate import tabulate
def print_time_table():
    print("wowowowowow")
def create_and_display_timetable():
    # Extracting time slots from the first day (assuming the same slots for each day)
    first_day_slots = emploi['Lundi']
    
    # Creating a timetable structure
    timetable = {day: [""] * len(first_day_slots) for day in emploi}

    # Displaying the timetable using tabulate
    headers = ["Jours"] + [f"Horaires {i+1}" for i in range(len(first_day_slots))]
    table_data = [(day, *slots) for day, slots in timetable.items()]

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))