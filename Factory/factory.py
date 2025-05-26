from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_motorcycle(self):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self) -> Vehicle:
        return Car("Ford", "Mustang (US Spec)")

    def create_motorcycle(self) -> Vehicle:
        return Motorcycle("Harley-Davidson", "Sportster (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self) -> Vehicle:
        return Car("Volkswagen", "Golf (EU Spec)")

    def create_motorcycle(self) -> Vehicle:
        return Motorcycle("BMW", "R1250 (EU Spec)")


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


def client_code(factory: VehicleFactory):
    car = factory.create_car()
    motorcycle = factory.create_motorcycle()

    car.start_engine()
    motorcycle.start_engine()


logging.info("US Vehicles:")
us_factory = USVehicleFactory()
client_code(us_factory)

logging.info("\nEU Vehicles:")
eu_factory = EUVehicleFactory()
client_code(eu_factory)
