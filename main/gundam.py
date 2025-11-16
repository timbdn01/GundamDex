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

