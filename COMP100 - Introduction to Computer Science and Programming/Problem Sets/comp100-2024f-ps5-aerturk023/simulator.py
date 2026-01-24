import random
from advanced_tires import AdvancedTires
from driver import Driver
from car import Car
from drs_car import DRSCar
from light_weight_body import LightweightBody
from track import Track
from race import Race
from turbo_charge import TurboCharge


if __name__ == '__main__':
    print("-----------------------------------------------------")
    print("--------------------- First Race --------------------")
    print("-----------------------------------------------------")
    random.seed(42)
    track = Track("Monza", 5.79, 11, 5)
    drivers = [Driver("Lewis Hamilton", 9, 0.2), Driver("Max Verstappen", 8, 0.25)]
    cars = [Car("Mercedes F1 W11", 360.0, 2.4, 9), Car("Red Bull RB16", 350.0, 2.4, 10)]
    number_of_laps = 5
    race = Race(track, drivers, cars, number_of_laps, "Sunny")

    for result in race.start_race():
        print(f"{result[0].name}: {result[1]:.2f} seconds")

    print("-----------------------------------------------------")
    print("-------------------- Second Race --------------------")
    print("-----------------------------------------------------")
    random.seed(42)
    setup_1 = TurboCharge() + LightweightBody() + AdvancedTires()
    setup_2 = LightweightBody() + AdvancedTires()
    track = Track("Monza", 5.79, 11, 5)
    drivers = [Driver("Lewis Hamilton", 9, 0.2), Driver("Max Verstappen", 8, 0.25), Driver("Charles Leclerc", 7, 0.3)]
    cars = [Car("Mercedes F1 W11", 360.0, 2.4, 9), Car("Red Bull RB16", 350.0, 2.4, 10), Car("Ferrari SF1000", 340.0, 2.5, 8)]
    cars[-1].add_component(setup_2) # Boost Leclerc's car
    cars[1].add_component(setup_1) # Boost Verstappen's car

    number_of_laps = 40
    race = Race(track, drivers, cars, number_of_laps, "Sunny")

    for result in race.start_race():
        print(f"{result[0].name}: {result[1]:.2f} seconds")

    print("-----------------------------------------------------")
    print("--------------------- Third Race --------------------")
    print("-----------------------------------------------------")
    random.seed(42)
    setup_1 = TurboCharge() + LightweightBody() + AdvancedTires()
    setup_2 = LightweightBody() + AdvancedTires()
    track = Track("Monza", 5.79, 11, 5)
    drivers = [Driver("Lewis Hamilton", 9, 0.2), Driver("Max Verstappen", 8, 0.25), Driver("Charles Leclerc", 7, 0.3)]
    cars = [DRSCar("Mercedes F1 W11", 360.0, 2.4, 9), DRSCar("Red Bull RB16", 350.0, 2.4, 10), DRSCar("Ferrari SF1000", 340.0, 2.5, 8)]
    cars[-1].add_component(setup_2) # Boost Leclerc's car
    cars[1].add_component(setup_1) # Boost Verstappen's car

    number_of_laps = 40
    race = Race(track, drivers, cars, number_of_laps, "Sunny")

    for result in race.start_race():
        print(f"{result[0].name}: {result[1]:.2f} seconds")
