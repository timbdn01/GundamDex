from gundam import Gundam
import os

def add_gundam(directory_path):
    print("Adding a new Gundam to the system.")
    name = input("Enter Gundam Name: ")
    model_number = input("Enter Model Number: ")
    pilot = input("Enter Pilot Name: ")
    weapons = input("Enter Weapons (comma separated): ").split(',')
    series = input("Enter Series Name: ")
    status = input("Enter Status (Active/Destroyed/Retired): ")
    try:
        height = float(input("Enter Height (in meters): "))
    except ValueError:
        height = None
    try:
        weight = float(input("Enter Weight (in tons): "))
    except ValueError:
        weight = None
    gunpla_available_input = input("Is Gunpla Available? (yes/no): ").strip().lower()
    gunpla_available = gunpla_available_input == 'yes'
    
    gunpla_grades = []
    if gunpla_available:
        grades_input = input("Enter Gunpla Grades (comma separated): ")
        gunpla_grades = [grade.strip() for grade in grades_input.split(',')]
    
    new_gundam = Gundam(
        name=name,
        model_number=model_number,
        pilot=pilot,
        weapons=[weapon.strip() for weapon in weapons],
        series=series,
        status=status,
        height=height,
        weight=weight,
        gunpla_available=gunpla_available,
        gunpla_grades=gunpla_grades
    )
    
    print("New Gundam added successfully!")
    print(new_gundam.display_info())
    create_txt_file(new_gundam, directory_path)
    
    return new_gundam

def create_txt_file(new_gundam, directory_path):
    file_name = f"{new_gundam.name.replace(' ', '_')}.txt"
    file_path = os.path.join(directory_path, file_name)
    try:
        with open(file_path, 'w') as file:
            file.write(new_gundam.display_info())
        print(f"Gundam data saved to {file_path}\n")
    except Exception as e:
        print(f"Error saving Gundam data to file: {e}\n")



