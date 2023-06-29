from manager.bicycle_manager import BicycleManager
from models.abstract_bicycle import AbstractBicycle
from models.bicycle import Bicycle
from models.electric_bicycle import ElectricBicycle
from models.electric_scooter import ElectricScooter
from models.gyro_scooter import GyroScooter


def main():
    bicycle_manager = BicycleManager()
    bicycle1 = Bicycle("road", "Corn", 60, 45, {"fast", "comfortable", "treat"})
    bicycle2 = Bicycle("mountain", "Xiaomi", 55, 38, {"cheap", "safe"})
    electric_bicycle1 = ElectricBicycle("road", "Vorskla", 60, 40, 35, 0.2, {"deadweight", "qualitative"})
    electric_bicycle2 = ElectricBicycle("road", "Xiaomi", 70, 30, 45, 0.6, {"economical", "effective"})
    electric_scooter1 = ElectricScooter("road", "Huawei", 30, 15, 2, 15, {"expensive", "lightweight"})
    electric_scooter2 = ElectricScooter("road", "Bolt", 40, 12, 3, 17, {"golden", "cool"})
    gyro_scooter1 = GyroScooter("mountain", "Glovo", 30, 10, 20, 36, 0.2, {"warden", "broken"})
    gyro_scooter2 = GyroScooter("road", "YoptaScooter", 50, 20, 30, 48, 0.5, {"old", "giant)"})

    bicycle_manager.add_bicycles(bicycle1)
    bicycle_manager.add_bicycles(bicycle2)
    bicycle_manager.add_bicycles(electric_bicycle1)
    bicycle_manager.add_bicycles(electric_bicycle2)
    bicycle_manager.add_bicycles(electric_scooter1)
    bicycle_manager.add_bicycles(electric_scooter2)
    bicycle_manager.add_bicycles(gyro_scooter2)
    bicycle_manager.add_bicycles(gyro_scooter1)

    print(bicycle_manager.zip_return())
    for bicycle in bicycle_manager.bicycles:
        attributes = AbstractBicycle.get_attributes_by_type(bicycle, int)
        print(attributes)

    def condition(some_bicycle):
        return isinstance(some_bicycle, Bicycle)

    print(bicycle_manager.all_and_any(condition))
    print(bicycle_manager.result_of_get_max_distance())
    print(bicycle_manager.enumerate_objects())
    print(bicycle2.__dict__)


if __name__ == "__main__":
    main()
