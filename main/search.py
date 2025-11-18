import os
def search_gundam(gundam_list):
    print("how would you like to search for a Gundam?")
    print("1. By Name")
    print("2. By Model Number")
    print("3. By Pilot")
    print("4. By Series")
    print("5. By Status")
    print("6. By Height")
    print("7. By Weight")
    print("8. By Gunpla Availability")
    input_choice = input("Enter your choice (1-8): ")
    search_results = []
    match input_choice:
        case '1':
            name = input("Enter Gundam Name to search: ").strip().lower()
            search_results = [g for g in gundam_list if g.name.lower() == name]
        case '2':
            model_number = input("Enter Model Number to search: ").strip().lower()
            search_results = [g for g in gundam_list if g.model_number.lower() == model_number]
        case '3':
            pilot = input("Enter Pilot Name to search: ").strip().lower()
            search_results = [g for g in gundam_list if g.pilot.lower() == pilot]
        case '4':
            series = input("Enter Series Name to search: ").strip().lower()
            search_results = [g for g in gundam_list if g.series.lower() == series]
        case '5':
            status = input("Enter Status (Active/Destroyed/Retired) to search: ").strip().lower()
            search_results = [g for g in gundam_list if g.status.lower() == status]
        case '6':
            height = float(input("Enter Height (in meters) to search: "))
            search_results = [g for g in gundam_list if g.height == height]
        case '7':
            weight = float(input("Enter Weight (in tons) to search: "))
            search_results = [g for g in gundam_list if g.weight == weight]
        case '8':
            gunpla_available_input = input("Is Gunpla Available? (yes/no): ").strip().lower()
            gunpla_available = gunpla_available_input == 'yes'
            search_results = [g for g in gundam_list if g.gunpla_available == gunpla_available]
        case _:
            print("Invalid choice. Returning to main menu.")
            return
    if not search_results:
        print("No Gundams found matching the search criteria.")
    else:
        print(f"Found {len(search_results)} Gundam(s):")
        for gundam in search_results:
            print(gundam.display_info())