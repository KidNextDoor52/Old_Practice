class Car:
    def __init__(self, make, model, year, color, vin=None):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.vin = vin

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Vin: {self.vin}")
        if self.vin:
            print(f"VIN: {self.vin}")

    def get_age(self, current_year):
        return current_year - self.year
    
    def repaint(self, new_color):
        self.color = new_color
        print(f"The {self.make} {self.model} has been repainted {self.color}.")



class Apt_pop:
    def __init__(self, start_date=None):
        self.star_date = start_date


class Residents(Apt_pop):
    def __init__(self, move_yr, unit_size, occup_num):
        super().__init__()
        self.move_yr = move_yr
        self.unit_size = unit_size
        self.occup_num = occup_num

Rob = Residents(2025, "2 BR", 2)

print(f"Rob's move in date is:  {Rob.move_yr}")

