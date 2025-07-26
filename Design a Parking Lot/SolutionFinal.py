# Parking Lot

# Relationships
#  --> ParkingLot HAS A Level
#  
"""
Entities --> ParkingLot, Levels, Spots, Vehicles

"""

class ParkingLot(): # whole system layout -- capacity
    pass

class Levels(): # track spots -- availability, parking, unpark
    pass

class ParkingSpot(): # track vehicles in a spot
    pass

from abc import ABC
class Vehicle(ABC): # vehicle information
    pass

class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
class Van(Vehicle):
    pass

"""
Relationships: 

Parking lot OWNS A level (composite)
Level OWNS A ParkingSpot (composite)
Parking Spot HAS A vehicle (aggregation)
Vehicle IS A Car, Bike, Van (Inheritance)

"""

"""
Functions :

parking lot --> assign levels, and spots

levels --> no. of available spots

parkingSpot --> search vehicle , park vehicle, unpark vehicle

"""