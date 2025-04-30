from spot_type import SpotType

class ParkingSpotManager:
    def __init__(self, spot_type):
        self.spot_type = spot_type
        self.available_spots = []
        self.occupied_spots = {}  # Key: license_plate, Value: ParkingSpot

    def add_parking_spot(self, spot):
        self.available_spots.append(spot)

    def park_vehicle(self, vehicle):
        for i, spot in enumerate(self.available_spots):
            if spot.can_fit_vehicle(vehicle):
                self.available_spots.pop(i)
                spot.park_vehicle(vehicle)
                self.occupied_spots[vehicle.license_plate] = spot
                return True
        return False  # No available spot that can fit the vehicle

# THis is pop default value input that is None here.
    def remove_vehicle(self, vehicle):
        spot = self.occupied_spots.pop(vehicle.license_plate, None)
        if spot:
            spot.remove_vehicle()
            self.available_spots.append(spot)
            return True
        return False  # Vehicle not found

    def get_total_available_spots(self):
        return len(self.available_spots)
