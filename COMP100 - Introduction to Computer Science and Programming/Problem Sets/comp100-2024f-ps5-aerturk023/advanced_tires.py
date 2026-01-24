from component import Component


class AdvancedTires(Component):
    def __init__(self):
        """
        Initializes a AdvancedTires object.
        """

        # TODO: Call the parent class's __init__ method and pass the name of the component
        super().__init__("AdvancedTires")

    def apply(self, car):
        """
        Apply the AdvancedTires component's effect to the car.

        Parameters:
            car (Car): The car to apply the AdvancedTires component to.
        """

        # TODO: Improve handling by 2
        car.handling += 2
