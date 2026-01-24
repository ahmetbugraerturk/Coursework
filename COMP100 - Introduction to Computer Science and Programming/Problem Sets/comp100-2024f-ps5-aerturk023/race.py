import random
from driver import Driver
from car import Car
from drs_car import DRSCar
from track import Track


class Race:
    def __init__(self, track: Track, drivers: list[Driver], cars: list[Car | DRSCar], number_of_laps: int, weather_condition: str):
        """
        Initializes a Race object.

        Parameters:
            track (Track): The racing track.
            drivers (list[Driver]): List of drivers participating in the race.
            cars (list[Car]): List of cars used in the race.
            number_of_laps (int): Total number of laps in the race.
            weather_condition (str): Current weather condition ("Sunny", "Rainy", "Foggy").

        Raises:
            TypeError: If track is not a Track object.
            TypeError: If any driver is not a Driver object.
            TypeError: If any car is not a Car or DRSCar object.
            TypeError: If number of laps is not an integer.
            ValueError: If weather condition is not "Sunny", "Rainy", or "Foggy".
        """
        # TODO: Check for type errors
        if not isinstance(track, Track):
            raise TypeError("If track is not a Track object.")
        if not isinstance(drivers, list) or type(drivers[0]) != Driver:
            raise TypeError("If any driver is not a Driver object.")
        if not isinstance(cars, list) or type(cars[0]) not in (Car, DRSCar):
            raise TypeError("If any car is not a Car or DRSCar object.")
        if not isinstance(number_of_laps, int):
            raise TypeError("If number of laps is not an integer.")


        # TODO: Check for value errors
        if weather_condition not in ("Sunny", "Rainy", "Foggy"):
            raise ValueError('If weather condition is not "Sunny", "Rainy", or "Foggy".')


        # TODO: Set instance variables
        self.track = track
        self.drivers = drivers
        self.cars = cars
        self.number_of_laps = number_of_laps
        self.weather_condition = weather_condition

    def start_race(self) -> list[tuple[Driver, float]]:
        """
        Simulates the race and determines the winner based on the total time taken by each driver.

        Use the Race Simulation Formula in for loop to calculate the total time taken by each driver.

        Returns:
            list: Sorted list of drivers and their total race times (lowest to highest).
        """

        # race_results should be a list of tuples where each tuple contains a Driver object and their total time
        race_results: list[tuple[Driver, float]] = []

        # TODO: Implement the race simulation formula
        w = {"Sunny": 1, "Rainy": 1.1, "Foggy": 1.15}[self.weather_condition]
        track_length = self.track.lap_length
        ass_d_c = {self.drivers[i]: self.cars[i] for i in range(len(self.drivers))}
        race_results = [[self.drivers[i], 0] for i in range(len(self.drivers))]
        for l in range(1, self.number_of_laps+1):
            lap_times = []
            for i in range(len(race_results)):
                car = ass_d_c[race_results[i][0]]
                driver = race_results[i][0]
                if type(car) == DRSCar and w == 1 and l>=2 and i!=0 and (race_results[i][1]-race_results[i-1][1])<1:
                    car.activate_drs()
                time = car.calculate_lap_time(track_length)
                time *= (1-(0.002*driver.experience))
                time += driver.reaction_time
                time *= w
                if random.random()<0.2:
                    time += self.random_event_time(driver.experience)
                if type(car) == DRSCar:
                    car.deactivate_drs()
                lap_times.append(time)
            for i in range(len(lap_times)):
                race_results[i][1] += lap_times[i]
            race_results.sort(key = lambda x: x[1])

        return race_results

    def random_event_time(self, experience) -> int:
        # TODO: Get and event_number between 1 and 5
        event_number = random.randint(1, 5)
            
        # TODO: Return the time based on the event_number
        time = 0
        if experience<3 and random.random()<0.375 and event_number!=5:
            #return True #for probability check
            time += random.randint(10, 30)
        
        match event_number:
            case 1:
                return time + random.randint(5, 15)
            case 2:
                return time + random.randint(3, 10)
            case 3:
                return time + random.randint(4, 8)
            case 4:
                return time + 20
            case 5:
                if experience < 3:
                    #return True #for probability check
                    return random.randint(10, 30)
                else:
                    return 0

                
            
            
        

"""
print("--- Probability check of occuring pit stop if drivers with experience < 3 ---")

track = Track("Monza", 5.79, 11, 5)
drivers = [Driver("Max Verstappen", 8, 0.25), Driver("Charles Leclerc", 6, 0.22), Driver("Lewis Hamilton", 10, 0.2)]
cars = [Car("Red Bull RB16", 350.0, 2.5, 8), Car("Ferrari F1", 350.0, 2.6, 8), Car("Mercedes F1 W11", 360.0, 2.4, 10)]
drs_cars = [DRSCar("Red Bull RB16", 350.0, 2.5, 8), DRSCar("Ferrari F1", 350.0, 2.6, 8), DRSCar("Mercedes F1 W11", 360.0, 2.4, 10)]
number_of_laps = 20
race = Race(track, drivers, cars, number_of_laps, "Sunny")

a=0
it= 10**6
for i in range(it):
    if random.random()<0.2:
        if race.random_event_time(2)==True:
            a+=1
print(a/it)

"""

        