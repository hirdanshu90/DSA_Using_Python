from abc import ABC, abstractmethod
import time
import math
from vehicle import VehicleType


# Using Strategy pattern

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, ticket):
        pass

class DefaultPricingStrategy(PricingStrategy):
    def __init__(self, flat_rate):
        self.flat_rate = flat_rate

    def calculate_fee(self, ticket):
        return self.flat_rate

class HourlyPricingStrategy(PricingStrategy):
    def __init__(self, rates_per_hour):
        self.rates_per_hour = rates_per_hour  # Dictionary: VehicleType -> rate_per_hour
        
        
# ticket: This is a reference to a ParkingTicket object.
    def calculate_fee(self, ticket):
        current_time = time.time()
        duration = current_time - ticket.issue_time
        hours = math.ceil(duration / 3600)
        vehicle_type = ticket.vehicle.get_vehicle_type()
        rate_per_hour = self.rates_per_hour.get(vehicle_type, 0)
        fee = rate_per_hour * hours
        return fee

class MinuteWisePricingStrategy(PricingStrategy):
    def __init__(self, rates_per_minute):
        self.rates_per_minute = rates_per_minute  # Dictionary: VehicleType -> rate_per_minute

    def calculate_fee(self, ticket):
        current_time = time.time()
        duration = current_time - ticket.issue_time
        minutes = math.ceil(duration / 60)
        vehicle_type = ticket.vehicle.get_vehicle_type()
        rate_per_minute = self.rates_per_minute.get(vehicle_type, 0)
        fee = rate_per_minute * minutes
        return fee
