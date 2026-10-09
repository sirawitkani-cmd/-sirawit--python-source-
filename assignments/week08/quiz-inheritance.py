""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def get__info(self):
        return f"Vehicle info: \nBrand:{self.Brand}, Model:{self.Model.}, Year{self.Year}"

class car(vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year):
        self.number_of_doors = number_of_doors
    def get__info(self):
        return f"Vehicle info: \nBrand:{self.Brand}, Model:{self.Model.}, Year:{self.Year}, number_of_doors:{self.number_of_doors}"
