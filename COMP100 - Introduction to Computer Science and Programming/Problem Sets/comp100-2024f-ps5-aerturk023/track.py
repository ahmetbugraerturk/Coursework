class Track:
    def __init__(self, name: str, lap_length: float, number_of_turns: int, difficulty: int) -> None:
        """
        Initializes a Track object.

        Parameters:
            name (str): Track name.
            lap_length (float): Lap length in km, in range [3.33, 7.0] km.
            number_of_turns (int): Total turns, 10-27.
            difficulty (int): Difficulty level, from 1 (Easy) to 10 (Hard).

        Raises:
            TypeError: If name is not a string.
            TypeError: If lap_length is not a float.
            TypeError: If number_of_turns is not an integer.
            TypeError: If difficulty is not an integer.
            ValueError: If lap_length is not in range [3.33, 7.0].
            ValueError: If number_of_turns is not in range 10-27.
            ValueError: If difficulty is not in range 1-10.
        """
        # TODO: Check for type errors
        if not isinstance(name, str):
            raise TypeError("If name is not a string.")
        if not isinstance(lap_length, float):
            raise TypeError("If lap_length is not a float.")
        if not isinstance(number_of_turns, int):
            raise TypeError("If number_of_turns is not an integer.")
        if not isinstance(difficulty, int):
            raise TypeError("If difficulty is not an integer.")

        # TODO: Check for value errors
        if lap_length<3.33 or lap_length>7.0:
            raise ValueError("If lap_length is not in range [3.33, 7.0].")
        if number_of_turns<10 or number_of_turns>27:
            raise ValueError("If number_of_turns is not in range 10-27.")
        if difficulty<1 or difficulty>10:
            raise ValueError("If difficulty is not in range 1-10.")


        # TODO: Set instance variables
        self.name = name
        self.lap_length = lap_length
        self.number_of_turns = number_of_turns
        self.difficulty = difficulty

    def __str__(self) -> str:
        """
        Returns a string representation of the track.

        Returns:
            str: Track's details.
        """
        # TODO: Return string representation
        return f"{self.name}, Lap Length: {self.lap_length} km, Number of Turns: {self.number_of_turns}, Difficulty: {self.difficulty}"

