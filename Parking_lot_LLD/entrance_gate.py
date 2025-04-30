from pricing_strategy_factory import PricingStrategyFactory
from parking_ticket import ParkingTicket

class EntranceGate:
    def __init__(self, gate_id, parking_lot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot

    def vehicle_enter(self, vehicle):
        # Obtain the pricing strategy from the factory
        pricing_strategy = PricingStrategyFactory.get_pricing_strategy(vehicle.get_vehicle_type())

        # Try to park the vehicle via ParkingLot
        if self.parking_lot.park_vehicle(vehicle):
            # Issue a ticket with the pricing strategy
            ticket = ParkingTicket(vehicle, pricing_strategy)
            print(f"Ticket issued: {ticket.ticket_number} for vehicle {vehicle.license_plate}")
            return ticket
        else:
            print("Parking Lot Full or No Suitable Spot")
            return None
