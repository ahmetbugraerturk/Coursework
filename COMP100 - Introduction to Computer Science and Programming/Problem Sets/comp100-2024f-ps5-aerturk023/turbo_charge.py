from car import Car
from component import Component


class TurboCharge(Component):
    def __init__(self):
        """
        Initializes a TurboCharge object.
        """
        super().__init__("TurboCharge")

    def apply(self, car: Car):
        """
        Apply the TurboCharge component's effect to the car.

        Parameters:
            car (Car): The car to apply the TurboCharge component to.
        """

        # TODO: Increase top speed by 5%
        car.top_speed *= 1.05