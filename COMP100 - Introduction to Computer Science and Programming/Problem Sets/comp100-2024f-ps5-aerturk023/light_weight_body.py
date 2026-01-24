from component import Component


class LightweightBody(Component):
    def __init__(self):
        """
        Initializes a LightweightBody object.
        """

        # TODO: Call the parent class's __init__ method and pass the name of
        super().__init__("LightweightBody")

    def apply(self, car):
        """
        Apply the LightweightBody component's effect to the car.

        Parameters:
            car (Car): The car to apply the LightweightBody component to.
        """

        # TODO: Improve acceleration time by 5%
        car.acceleration *= .95