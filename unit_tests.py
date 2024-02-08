import unittest
from main import generate_successors
from pitcher import Pitcher
from informed_search_a_star import heuristic

class Test_Generate_Successors_Starting_Empty(unittest.TestCase):
    def test_generate_successors(self):
        # Initialize a test case with a simple set of pitchers
        pitchers = [Pitcher(3, 0), Pitcher(5, 0), Pitcher(8, 0)]
        
        # Generate successors
        successors = generate_successors(pitchers)

        # Print each generated state for visual inspection
        print("\nGenerated States:")
        for state in successors:
            print([f"Pitcher(capacity={p.capacity}, current_volume={p.current_volume})" for p in state])

        # Verify the number of generated states
        self.assertEqual(len(successors), len(pitchers), "Should generate an equal number of valid successor states for the given initial state based on the number of empty pitchers.")
        
        # Additional checks for state correctness could be added here based on expected outcomes

def test_heuristic_with_successors():
    capacities = [3, 5, 8]  # Example capacities
    target = 143  # Example target quantity
    
    # Initialize a test case with a simple set of pitchers
    pitchers = [Pitcher(capacity, 0) for capacity in capacities]
    
    # Generate successors
    successors = generate_successors(pitchers)
    
    print(f"Testing Heuristic with Target: {target} and Capacities: {capacities}\n")
    for successor in successors:
        # Assuming successor is a list of Pitcher objects
        current_volumes = [pitcher.current_volume for pitcher in successor]
        total_volume = sum(current_volumes)
        h_value = heuristic(target - total_volume, capacities)  # Adjust heuristic calculation if necessary
        print(f"Successor State: {[f'Pitcher(capacity={p.capacity}, current_volume={p.current_volume})' for p in successor]}, Heuristic Estimate: {h_value}")

if __name__ == '__main__':
    test_heuristic_with_successors()