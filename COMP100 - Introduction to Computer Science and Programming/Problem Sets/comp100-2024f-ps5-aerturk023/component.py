from car import Car


class Component:
    def __init__(self, name: str) -> None:
        """
        Initializes a Component object

        Parameters:
            name (str): The name of the component.
        """
        # TODO: Set the name of the component
        self.name = name

    def apply(self, car: Car) -> None:
        """
        Apply the component's effect to the car.

        Parameters:
            car (Car): The car to apply the component to.

        Raises:
            NotImplementedError: This method must be implemented in the subclass.
        """
        raise NotImplementedError("Each component must define an apply method.")

    def __add__(self, other):
        """
        Add two components together to create a composite component.

        Parameters:
            other (Component): The other component to add.

        Returns:
            CompositeComponent: The composite component created by adding the two components.

        Raises:
            TypeError: If the other object is not a Component object.
        """

        # TODO: Check for type error
        if not isinstance(other, Component):
            raise TypeError("If the other object is not a Component object.")


        # TODO: Return a CompositeComponent object with self and other as components
        return CompositeComponent(self, other)
        

class CompositeComponent(Component):
    def __init__(self, *components) -> None:
        """
        Initializes a CompositeComponent object.

        Parameters:
            components (any): Single or combined (Composite) components (not a Python list)
        """
        super().__init__("Composite")

        # TODO: Set the components of the composite component
        self.components = components

    def apply(self, car: Car) -> None:
        """
        Apply the composite component's effect to the car.

        Parameters:
            car (Car): The car to apply the composite component to.
        """

        # TODO: Apply each component in the list of components to the car
        for c in self.components:
            c.apply(car)
