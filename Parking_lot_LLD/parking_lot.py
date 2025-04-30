from parking_spot import TwoWheelerSpot, FourWheelerSpot, LargeSpot
from parking_spot_manager import ParkingSpotManager
from spot_type import SpotType

class ParkingLot:
    def __init__(self, num_two_wheeler_spots, num_four_wheeler_spots, num_large_spots):
        self.parking_spot_managers = {}
        self._init_spots(num_two_wheeler_spots, num_four_wheeler_spots, num_large_spots)



    def _init_spots(self, num_two_wheeler_spots, num_four_wheeler_spots, num_large_spots):
        spot_id = 0

        # Two-Wheeler Spots
        two_wheeler_manager = ParkingSpotManager(SpotType.TWO_WHEELER_SPOT)
        for _ in range(num_two_wheeler_spots):
            spot = TwoWheelerSpot(spot_id)
            two_wheeler_manager.add_parking_spot(spot)
            spot_id += 1
        self.parking_spot_managers[SpotType.TWO_WHEELER_SPOT] = two_wheeler_manager

        # Four-Wheeler Spots
        four_wheeler_manager = ParkingSpotManager(SpotType.FOUR_WHEELER_SPOT)
        for _ in range(num_four_wheeler_spots):
            spot = FourWheelerSpot(spot_id)
            four_wheeler_manager.add_parking_spot(spot)
            spot_id += 1
        self.parking_spot_managers[SpotType.FOUR_WHEELER_SPOT] = four_wheeler_manager

        # Large Spots
        large_spot_manager = ParkingSpotManager(SpotType.LARGE_SPOT)
        for _ in range(num_large_spots):
            spot = LargeSpot(spot_id)
            large_spot_manager.add_parking_spot(spot)
            spot_id += 1
        self.parking_spot_managers[SpotType.LARGE_SPOT] = large_spot_manager

    def park_vehicle(self, vehicle):
        spot_type = vehicle.get_required_spot_type()
        manager = self.parking_spot_managers.get(spot_type)
        if manager and manager.park_vehicle(vehicle):
            return True
        else:
            return False  # No suitable spot available

    def remove_vehicle(self, vehicle):
        spot_type = vehicle.get_required_spot_type()
        manager = self.parking_spot_managers.get(spot_type)
        if manager and manager.remove_vehicle(vehicle):
            return True
        else:
            return False  # Vehicle not found

    def get_available_spots(self):
        return sum(manager.get_total_available_spots() for manager in self.parking_spot_managers.values())
