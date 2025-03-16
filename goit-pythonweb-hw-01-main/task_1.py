from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region or ""

    def start_engine(self):
        logging.info(f"{self.make} {self.model} {self.region}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region or ""

    def start_engine(self):
        logging.info(f"{self.make} {self.model} {self.region}: Мотор запущено")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str):
        return Car(make, model, "(EU Spec)")

    def create_motorcycle(self, make: str, model: str):
        return Motorcycle(make, model, "(EU Spec)")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str):
        return Car(make, model, "(US Spec)")

    def create_motorcycle(self, make: str, model: str):
        return Motorcycle(make, model, "(US Spec)")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

us_car = us_factory.create_car("Ford", "Mustang")
eu_car = eu_factory.create_car("Volkswagen", "Golf")

us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1250GS")

us_car.start_engine()
eu_car.start_engine()
us_motorcycle.start_engine()
eu_motorcycle.start_engine()
