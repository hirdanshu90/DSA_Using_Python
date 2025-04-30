from abc import ABC, abstractmethod
from enum import Enum
from spot_type import SpotType

class VehicleType(Enum):
    MOTORBIKE = 'Motorbike'
    CAR = 'Car'
    BUS = 'Bus'
    TRUCK = 'Truck'

class Vehicle(ABC):
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.parking_spot = None  # Assigned when the vehicle is parked

    @abstractmethod
    def get_required_spot_type(self):
        pass

    @abstractmethod
    def get_vehicle_type(self):
        pass

class Motorbike(Vehicle):
    def get_required_spot_type(self):
        return SpotType.TWO_WHEELER_SPOT

    def get_vehicle_type(self):
        return VehicleType.MOTORBIKE


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)
    def get_required_spot_type(self):
        return SpotType.FOUR_WHEELER_SPOT
    def get_vehicle_type(self):
        return VehicleType.CAR

class Bus(Vehicle):
    def get_required_spot_type(self):
        return SpotType.LARGE_SPOT

    def get_vehicle_type(self):
        return VehicleType.BUS

class Truck(Vehicle):
    def get_required_spot_type(self):
        return SpotType.LARGE_SPOT

    def get_vehicle_type(self):
        return VehicleType.TRUCK
