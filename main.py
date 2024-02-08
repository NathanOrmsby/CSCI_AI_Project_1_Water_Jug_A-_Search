import os
from pitcher import Pitcher
from state_stuff import initialize_state
from informed_search_a_star import a_star_search


def parse_input(filename):
    with open(filename, 'r') as file:
        # Read the first line to get the capacities
        capacities_line = file.readline().strip()
        # If there's only one capacity, convert it to a list with a single element
        if ',' not in capacities_line:
            capacities = [int(capacities_line)]
        else:
            capacities = list(map(int, capacities_line.split(',')))

        # Read the target volume from the second line
        target = int(file.readline().strip())

    return capacities, target



# Using the modified initialize_state function
if __name__ == "__main__":
    filename = os.path.join("Data", "cat_data_test_3.txt")
    capacities, target_volume = parse_input(filename)

    # Initialize pitchers with their capacities, assuming all start empty
    pitchers = initialize_state(capacities)
    start_state = tuple(p.current_volume for p in pitchers)  # Initial volumes of the pitchers

    # Start the search with an initial total volume poured of 0
    initial_total_volume_poured = 0

    print(f"Pitchers: {pitchers}")
    print(f"Target: {target_volume}")
    print(f"Capacities: {capacities}")
    print(f"Start state: {start_state}")
    print("Starting search...")

    # Adjust the call to include the initial total volume poured
    optimal_cost = a_star_search(start_state, 0, target_volume, capacities)

    if optimal_cost is not None:
        print(f"Optimal cost to reach the target volume: {optimal_cost}")
    else:
        print("No solution found.")
    
