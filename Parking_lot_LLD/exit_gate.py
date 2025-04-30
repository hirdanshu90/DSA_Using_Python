from payment_processor import PaymentProcessor

class ExitGate:
    def __init__(self, gate_id, parking_lot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot
        self.payment_processor = PaymentProcessor()

    def vehicle_exit(self, ticket):
        if not ticket.is_paid:
            fee = ticket.calculate_fee()
            # Process payment
            if self.payment_processor.process_payment(fee, "Credit Card"):
                ticket.pay_ticket(fee)
                print(f"Ticket {ticket.ticket_number} paid. Amount: {fee:.2f}")
            else:
                print("Payment failed")
                return False
        else:
            print(f"Ticket {ticket.ticket_number} already paid.")

        # Remove vehicle from parking spot
        vehicle = ticket.vehicle
        if self.parking_lot.remove_vehicle(vehicle):
            print(f"Vehicle {vehicle.license_plate} exited.")
            return True
        else:
            print("Error: Vehicle not found in the parking lot.")
            return False
