from abc import ABC, abstractmethod
from spot_type import SpotType

class ParkingSpot(ABC):
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.vehicle = None  # The vehicle currently parked in the spot

    def is_available(self):
        return self.vehicle is None

    @abstractmethod
    def get_spot_type(self):
        pass

# NICE check here.
    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.get_required_spot_type() == self.get_spot_type()

# update the spot if the vehicle is going to be parked there
    def park_vehicle(self, vehicle):
        if self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            vehicle.parking_spot = self
            return True
        return False

    def remove_vehicle(self):
        if self.vehicle:
            self.vehicle.parking_spot = None
            self.vehicle = None
            return True
        return False



class TwoWheelerSpot(ParkingSpot):
    def get_spot_type(self):
        return SpotType.TWO_WHEELER_SPOT

class FourWheelerSpot(ParkingSpot):
    def get_spot_type(self):
        return SpotType.FOUR_WHEELER_SPOT

class LargeSpot(ParkingSpot):
    def get_spot_type(self):
        return SpotType.LARGE_SPOT
