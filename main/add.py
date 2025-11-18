from gundam import Gundam

def add_gundam():
    print("Adding a new Gundam to the system.")
    name = input("Enter Gundam Name: ")
    model_number = input("Enter Model Number: ")
    pilot = input("Enter Pilot Name: ")
    weapons = input("Enter Weapons (comma separated): ").split(',')
    series = input("Enter Series Name: ")
    status = input("Enter Status (Active/Destroyed/Retired): ")
    height = float(input("Enter Height (in meters): "))
    weight = float(input("Enter Weight (in tons): "))
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
    
    return new_gundam