from pricing_strategy import DefaultPricingStrategy, HourlyPricingStrategy, MinuteWisePricingStrategy
from vehicle import VehicleType

class PricingStrategyFactory:
    @staticmethod
    def get_pricing_strategy(vehicle_type, criteria=None):
        if vehicle_type in [VehicleType.CAR, VehicleType.TRUCK]:
            hourly_rates = {
                VehicleType.CAR: 5,
                VehicleType.TRUCK: 15
            }
            return HourlyPricingStrategy(rates_per_hour=hourly_rates)
        elif vehicle_type == VehicleType.MOTORBIKE:
            minute_rates = {
                VehicleType.MOTORBIKE: 0.05
            }
            return MinuteWisePricingStrategy(rates_per_minute=minute_rates)
        elif vehicle_type == VehicleType.BUS:
            return DefaultPricingStrategy(flat_rate=20)
        else:
            return DefaultPricingStrategy(flat_rate=10)
