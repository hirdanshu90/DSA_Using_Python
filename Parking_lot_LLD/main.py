import time
from parking_lot import ParkingLot
from entrance_gate import EntranceGate
from exit_gate import ExitGate
from vehicle import Car, Motorbike, Bus, Truck

def main():
    # Create a parking lot with specific numbers of each spot type
    num_two_wheeler_spots = 20
    num_four_wheeler_spots = 50
    num_large_spots = 10
    parking_lot = ParkingLot(num_two_wheeler_spots, num_four_wheeler_spots, num_large_spots)

    # Create entrance and exit gates
    entrance_gate = EntranceGate("Entrance1", parking_lot)
    exit_gate = ExitGate("Exit1", parking_lot)

    # Vehicles entering
    car1 = Car("Porshe_spider ")
    ticket1 = entrance_gate.vehicle_enter(car1)

    bike1 = Motorbike("BIKE999")
    ticket2 = entrance_gate.vehicle_enter(bike1)

    bus1 = Bus("BUS777")
    ticket3 = entrance_gate.vehicle_enter(bus1)

    truck1 = Truck("TRUCK555")
    ticket4 = entrance_gate.vehicle_enter(truck1)

    # Check available spots
    print(f"Available spots: {parking_lot.get_available_spots()}")

    # Simulate time passage
    time.sleep(2)  # Simulate parking duration

    # Vehicles exiting
    if ticket1:
        exit_gate.vehicle_exit(ticket1)

    if ticket2:
        exit_gate.vehicle_exit(ticket2)

    if ticket3:
        exit_gate.vehicle_exit(ticket3)

    if ticket4:
        exit_gate.vehicle_exit(ticket4)

    # Check available spots after exit
    print(f"Available spots after exit: {parking_lot.get_available_spots()}")

if __name__ == "__main__":
    main()
