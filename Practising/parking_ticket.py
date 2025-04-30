import uuid
import time

class ParkingTicket():
    def __init__(self,vehicle, pricing_strategy):
        self.ticket_number = str(uuid.uuid4())
        self.vehicle = vehicle
        self.issue_time = time.time()
        self.pricing_strategy = pricing_strategy
        self.is_paid = False
        self.fee = 0
        self.pay_time = None


    def calculate_fee(self):
        self.fee = self.pricing_strategy.calculate_fee(fee)
        return self.fee
    
    def pay_ticket(self,amount):
        if amount >= self.fee:
            self.is_paid = True
            self.pay_time = time.time()
            return True
        return False