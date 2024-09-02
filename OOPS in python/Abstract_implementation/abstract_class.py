# DEfined the blue print for all the vehicles here....
# Should have atleast one abstract method to make it a abstract class...
# We can't instantiate Vehicle class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres = n
    @abstractmethod
    def start(self):
        pass

