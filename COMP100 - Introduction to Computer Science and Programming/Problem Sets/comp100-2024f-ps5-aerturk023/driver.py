class Driver:
    def __init__(self, name: str, experience: int, reaction_time: float) -> None:
        """
        Initializes a Driver object.

        Parameters:
            name (str): The driver's name.
            experience (int): Experience level, 1-10 (1: Novice, 10: Expert).
            reaction_time (float): Reaction time in seconds, between [0.1, 1.0] (0.1: Expert, 1.0: Novice).

        Raises:
            TypeError: If name is not a string.
            TypeError: If experience is not an integer.
            TypeError: If reaction_time is not a float.
            ValueError: If experience is not in range 1-10.
            ValueError: If reaction_time is not in range [0.1, 1.0].
        """
        # TODO: Check for type errors
        if not isinstance(name, str):
            raise TypeError("If name is not a string.")
        if not isinstance(experience, int):
            raise TypeError("If experience is not an integer.")
        if not isinstance(reaction_time, float):
            raise TypeError("If reaction_time is not a float.")

        # TODO: Check for value errors
        if experience<1 or experience>10:
            raise ValueError("If experience is not in range 1-10.")
        if reaction_time<0.1 or reaction_time>1.0:
            raise ValueError("If reaction_time is not in range [0.1, 1.0].")


        # TODO: Set instance variables
        self.name = name
        self.experience = experience
        self.reaction_time = reaction_time
        
        

    def __str__(self) -> str:
        """
        Returns a string representation of the Driver object.

        Returns:
            str: The string representation of the Driver.
        """
        # TODO: Implement this method
        return f"{self.name}, Experience: {self.experience}, Reaction Time: {self.reaction_time}s"
