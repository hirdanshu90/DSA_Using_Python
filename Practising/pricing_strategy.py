from abc import ABC, abstractmethod
import time
import math
from vehicle import VehicleType

Using 

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self,ticket):
        pass

class defaultPricingStrategy(PricingStrategy):
    def __init__(self,flat_rate):
        self.flat_rate = flat_rate

    def calculate_fee(self, ticket):
        return self.flat_rate
    

class MinuteWisePricingStrategy(PricingStrategy):
    def __init__(self,rate_per_minute):
        self.rate_per_minute = rate_per_minute

    def calculate_fee(self, ticket):
        current_time = time.time()
        duration = current_time - ticket.issue_time
        minutes = math.ceil(duration/60)
        vehicle_type = ticket.vehicle.get_vehicle_type()
        rate_per_minute = self.rate_per_minute.get(vehicle_type,0)
        fee = rate_per_minute * minutes
        return fee

class HourlyPricingStrategy(PricingStrategy):
    def __init__(self, rates_per_hour):
        self.rates_per_hour = rates_per_hour  # Dictionary: VehicleType -> rate_per_hour

    def calculate_fee(self, ticket):
        current_time = time.time()
        duration = current_time - ticket.issue_time
        hours = math.ceil(duration / 3600)
        vehicle_type = ticket.vehicle.get_vehicle_type()
        rate_per_hour = self.rates_per_hour.get(vehicle_type, 0)
        fee = rate_per_hour * hours
        return fee
