from manager.bicycle_manager import BicycleManager
from models.bicycle import Bicycle
from models.electric_bicycle import ElectricBicycle
from models.electric_scooter import ElectricScooter
from models.gyro_scooter import GyroScooter


def main():

    bicycle_manager = BicycleManager()

    bicycle1 = Bicycle("road", "Vor", 65, 35, {"slow", "tiny"})
    bicycle2 = Bicycle("mountain", "Default", 50, 120, {"fast", "cool"})
    electric_bicycle1 = ElectricBicycle("road", "Drifter", 64, 43, 23, 0.2, {"bright", "cheap"})
    electric_bicycle2 = ElectricBicycle("mountain", "Mini", 70, 13, 45, 0.6, {"deadweight", "eats coal"})
    electric_scooter1 = ElectricScooter("road", "Bolt", 20, 5, 3, 15)
    electric_scooter2 = ElectricScooter("mountain", "AntiBolt", 40, 10, 6, 34)
    gyro_scooter1 = GyroScooter("mountain", "Xiaomi", 30, 10, 20, 36, 0.2)
    gyro_scooter2 = GyroScooter("road", "Samson", 50, 20, 30, 48, 0.5)

    bicycle_manager.add_bicycles(bicycle1)
    bicycle_manager.add_bicycles(bicycle2)
    bicycle_manager.add_bicycles(electric_bicycle1)
    bicycle_manager.add_bicycles(electric_bicycle2)
    bicycle_manager.add_bicycles(electric_scooter1)
    bicycle_manager.add_bicycles(electric_scooter2)
    bicycle_manager.add_bicycles(gyro_scooter1)
    bicycle_manager.add_bicycles(gyro_scooter2)

    for bicycle in bicycle_manager.bicycles:
        print(bicycle)
    print("\n")

    bicycles_speed_more_than = bicycle_manager.find_bicycles_with_max_speed_more_than(60)
    bicycles_with_brand = bicycle_manager.find_bicycles_by_brand("Vor")

    print("Bicycles with max speed more than 60 : ")
    for bicycle in bicycles_speed_more_than:
        print(bicycle)
    print("\n")

    print("Bicycles with brand \"Vor\" : ")
    for bicycle in bicycles_with_brand:
        print(bicycle)
        print("\n")


if __name__ == "__main__":
    main()
