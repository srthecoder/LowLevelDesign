# Design a parking Lot

#  what functionalities would you like it to perform?
# --> search spot , park, remove

# vehicle --> Parking lot --> find a spot --> park / unpark
# do we have multiple types of vehicles? --> car, bike, van
from enum import Enum
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    VAN = 3
    
from abc import ABC
class Vehicle(ABC):
    def __init__(self, model, color, licensePlate):
        self.model = model
        self.color = color
        self.licensePlate = licensePlate

class Car(Vehicle):
    def __init__(self, model, color, licensePlate):
        super().__init__( model, color, licensePlate)
        self.vehicle_type = VehicleType.CAR
        
class Bike(Vehicle):
    def __init__(self, model, color, licensePlate):
        super().__init__( model, color, licensePlate)
        self.vehicle_type = VehicleType.BIKE

class VAN(Vehicle):
    def __init__(self, model, color, licensePlate):
        super().__init__( model, color, licensePlate)
        self.vehicle_type = VehicleType.VAN

        
class Levels(): # levels have parking spots
    n_levels = 0 #keeps count of levels in our lot
    level = dict()
    def __init__(self, n_spots):
        self.n_spots = n_spots
        Levels.n_levels += 1 # new level created
        Levels.level[Levels.n_levels] = [None]*n_spots
        # level --> {1:[None, None, None], 2:[None, None]}

    @staticmethod
    def is_available(levelNo, SpotId): #check for availability
        if levelNo and levelNo <= Levels.n_levels and SpotId < len(Levels.level[levelNo]):
            if Levels.level[levelNo][SpotId] is None:
                return f"Spot {SpotId} at level {levelNo} is available."
            else:
                return f"Spot {SpotId} at level {levelNo} is unavailable."
        else:
            return f"Invalid Spot!"
        
    def parking(self, license_plate):
        for k, v in self.level.items():
            if len(v)+1 < self.n_spots:
                self.level[k].append(license_plate)
                print("Vehicle has been parked.")
                break
        print("Sorry, Parking Lot is full. ")
        
    def unpark(self, license_plate):
        for k, v in self.level.items():
            if license_plate in v:
                self.level[k].remove(license_plate)
                print("Vehicle has exited the parking lot.")
        print("Vehicle not found.")
        
class ParkingLot(Levels): # have vehicles
    def __init__(self, n_spots):
        super().__init__(n_spots)
            
    
    

p1 = ParkingLot(5) 
p2 = ParkingLot(2)
print(p1.level)
print(p2.level)

print(Levels.is_available(2, 1))
print(Levels.is_available(3, 1))


c1 = Car("Porsche", "Red", "ABCD123")
c2 = Car("Mercedes", "White", "XYZ456")

ParkingLot.parking(p1, c1.licensePlate)
ParkingLot.parking(p2, c2.licensePlate)
print(p1.level)
print(p2.level)
