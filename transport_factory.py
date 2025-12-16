from car import Car
from bike import Bike

class TransportFactory:
    def create_transport(self, transport_type):
        if transport_type == "car":
            return Car()
        elif transport_type == "bike":
            return Bike()
