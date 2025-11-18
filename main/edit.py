def edit_gundam_info(gundam_id):
    print(f"Editing information for {gundam_id.name}. Leave blank to keep current value.\n")
    new_name = input(f"Enter new Name (current: {gundam_id.name}): ").strip()
    if new_name:
        gundam_id.name = new_name
    new_model_number = input(f"Enter new Model Number (current: {gundam_id.model_number}): ").strip()
    if new_model_number:
        gundam_id.model_number = new_model_number
    new_pilot = input(f"Enter new Pilot (current: {gundam_id.pilot}): ").strip()
    if new_pilot:
        gundam_id.pilot = new_pilot
    new_weapons = input(f"Enter new Weapons (comma separated) (current: {', '.join(gundam_id.weapons)}): ").strip()
    if new_weapons:
        gundam_id.weapons = [weapon.strip() for weapon in new_weapons.split(',')]
    new_series = input(f"Enter new Series (current: {gundam_id.series}): ").strip()
    if new_series:
        gundam_id.series = new_series
    new_status = input(f"Enter new Status (current: {gundam_id.status}): ").strip()
    if new_status:
        gundam_id.status = new_status
    new_height = input(f"Enter new Height in meters (current: {gundam_id.height}): ").strip()
    if new_height:
        gundam_id.height = float(new_height)
    new_weight = input(f"Enter new Weight in tons (current: {gundam_id.weight}): ").strip()
    if new_weight:
        gundam_id.weight = float(new_weight)
    gunpla_available_input = input(f"Is Gunpla Available? (yes/no) (current: {'yes' if gundam_id.gunpla_available else 'no'}): ").strip().lower()
    if gunpla_available_input:
        gundam_id.gunpla_available = gunpla_available_input == 'yes'
        if gundam_id.gunpla_available:
            grades_input = input(f"Enter Gunpla Grades (comma separated) (current: {', '.join(gundam_id.gunpla_grades) if gundam_id.gunpla_grades else 'None'}): ").strip()
            if grades_input:
                gundam_id.gunpla_grades = [grade.strip() for grade in grades_input.split(',')]
        else:
            gundam_id.gunpla_grades = None
    print("Gundam information updated successfully!\n")
    