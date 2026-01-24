import os
import ps3c

def allocate_resources(houses_file, assignments_file, white_walkers):
    """
    Allocates resources (soldiers and weapons) to gates based on White Walker threats.

    Parameters:
        houses_file (str): Path to the file containing house resources.
        assignments_file (str): Path to the file containing gate assignments.
        white_walkers (dict): Dictionary specifying the White Walker threat levels for each gate.

    Outputs:
        Writes updated files to `solution_outputs/final_houses_file.txt` and `solution_outputs/final_assignments_file.txt`.
    """

    def parse_input_file(file_path):
        """
        Parses the input file into a dictionary.
        
        Returns:
            dict: Parsed data from the file.
        """
        return ps3c.txt_to_dict(file_path)

    def save_output_file(data, file_path):
        """
        Saves the dictionary into the file in the specified format.
        
        Parameters:
            data (dict): Data to write into the file.
            file_path (str): Path where the file will be saved.
        """
        with open(file_path, "w") as path:
            for k,v in data.items():
                path.write(f"{k}: {v}\n")

    def binary_search_exact_match(houses, required_key, required_value):
        """
        Finds a house with exactly the required resources using binary search.
        
        Returns:
            tuple: (house_name, resources) or (None, None) if no match is found.
        """
        houses = sorted(houses.items(), key=lambda x: x[1][required_key])
        low = 0
        high = len(houses)-1
        guess = (low+high)//2
        iteration = len(houses)//2+1
        for i in range(iteration):
            if houses[guess][1][required_key] != required_value:
                if required_value<houses[guess][1][required_key]:
                    high = guess+1
                elif required_value>houses[guess][1][required_key]:
                    low = guess-1
                guess = (low+high)//2
            else:                
                return houses[guess][0], houses[guess][1][required_key]
        return (None, None)

    def allocate_reinforcements(gates, houses, resource_key):
        """
        Allocates reinforcements for gates based on the resource key.
        
        Parameters:
            gates (dict): Dictionary containing gate resources.
            houses (dict): Dictionary containing house resources.
            resource_key (str): The type of resource to allocate (e.g., "soldiers" or "weapons").
        
        Returns:
            tuple: Updated gates and houses dictionaries.
        """
        # TODO: Implement the logic to allocate resources from houses to gates.
        for k,v in gates.items():
            req_val = white_walkers[k]-v[resource_key]
            h, r = binary_search_exact_match(houses, resource_key, req_val)
            gates[k][resource_key] += r
            houses[h][resource_key] = 0
        save_output_file(gates, assignments_file)
        save_output_file(houses, houses_file)
        return gates, houses
    
    # Parse input files for houses and gate assignments.
    houses = parse_input_file(houses_file)
    gates = parse_input_file(assignments_file)

    # Allocate soldiers and weapons.
    gates, houses = allocate_reinforcements(gates, houses, "soldiers")
    gates, houses = allocate_reinforcements(gates, houses, "weapons")
    
    # Save updated data to output files.
    save_output_file(houses, "solution_outputs/final_houses.txt")
    save_output_file(gates, "solution_outputs/final_assignments.txt")
