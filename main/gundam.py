class Gundam:
    def __init__(self, name, model_number, pilot, weapons, series, status, height, weight, gunpla_available, gunpla_grades=None):
        self.name = name
        self.model_number = model_number
        self.pilot = pilot
        self.weapons = weapons
        self.series = series
        self.status = status
        self.height = height  # in meters
        self.weight = weight  # in tons
        self.gunpla_available = gunpla_available  # Boolean
        self.gunpla_grades = gunpla_grades if gunpla_available else None

    def display_info(self):
        info = f"Gundam Name: {self.name}\n"
        info += f"Model Number: {self.model_number}\n"
        info += f"Pilot: {self.pilot}\n"
        info += f"Weapons: {', '.join(self.weapons)}\n"
        info += f"Series: {self.series}\n"
        info += f"Status: {self.status}\n"
        info += f"Height: {self.height} meters\n"
        info += f"Weight: {self.weight} tons\n"
        info += f"Gunpla Available: {'Yes' if self.gunpla_available else 'No'}\n"
        if self.gunpla_available:
            info += f"Gunpla Grades: {', '.join(self.gunpla_grades)}\n"
        return info
    def convert_from_text(self, text):
        lines = text.strip().split('\n')
        name = lines[0].split(': ')[1]
        model_number = lines[1].split(': ')[1]
        pilot = lines[2].split(': ')[1]
        weapons = lines[3].split(': ')[1].split(', ')
        series = lines[4].split(': ')[1]
        status = lines[5].split(': ')[1]
        height = (lines[6].split(': ')[1].split(' ')[0])
        weight = (lines[7].split(': ')[1].split(' ')[0])
        gunpla_available = lines[8].split(': ')[1] == 'Yes'
        gunpla_grades = []
        if gunpla_available:
            gunpla_grades = lines[9].split(': ')[1].split(', ')
        return Gundam(name, model_number, pilot, weapons, series, status, height, weight, gunpla_available, gunpla_grades)
