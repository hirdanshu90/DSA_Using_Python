from abc import ABC, abstractmethod

# Context
class TrafficLight:
    def __init__(self, state: TrafficLightState):
        self.state = state

    def request(self):
        self.state.handle(self)

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# Concrete State: Red Light
class RedLight(TrafficLightState):
    def handle(self, context):
        print("Red Light - Stop!")
        context.state = GreenLight()  # Switch to Green

# Concrete State: Green Light
class GreenLight(TrafficLightState):
    def handle(self, context):
        print("Green Light - Go!")
        context.state = YellowLight()  # Switch to Yellow

# Concrete State: Yellow Light
class YellowLight(TrafficLightState):
    def handle(self, context):
        print("Yellow Light - Slow down!")
        context.state = RedLight()  # Switch to Red



# Example usage:
if __name__ == "__main__":
    traffic_light = TrafficLight(RedLight())
    
    for _ in range(5):
        traffic_light.request()