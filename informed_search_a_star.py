from queue import PriorityQueue
from state_stuff import generate_successors
from pitcher import Pitcher
import time

def is_goal_state(pitchers, target_volume):
    total_volume_poured = sum(p.volume_poured_to_infinite for p in pitchers)
    return total_volume_poured == target_volume


# Total volume difference
def heuristic_volume_diff(state, target):
    total_volume = sum(state)
    # Calculate the absolute difference between the current total volume and the target volume
    return abs(total_volume - target)

# Reservoir filled
def heuristic_reservoir(total_volume_poured, target):
    # Calculate the absolute difference between the current total volume poured into the reservoir and the target volume
    return abs(total_volume_poured - target)

# Modulo capacity
def heuristic_modulo_capacity(capacities, target):
    return target % min(capacities)



def a_star_search(start_state, initial_total_volume_poured, target_volume, capacities):
    start_time = time.perf_counter()  # Start timing
    open_set = PriorityQueue()
    open_set.put((0, (start_state, initial_total_volume_poured)))
    print(f"Starting A* search with start state: {start_state}, target volume: {target_volume}")

    cost_so_far = {(start_state, initial_total_volume_poured): 0}
    max_capacity = max(capacities)  # Find the maximum capacity of the pitchers

    while not open_set.empty():
        _, (current_state_tuple, current_total_volume_poured) = open_set.get()

        if current_total_volume_poured == target_volume:
            end_time = time.perf_counter()  # End timing
            elapsed_time = (end_time - start_time) * 1000
            print(f"Goal state reached: {current_state_tuple} with total cost: {cost_so_far[(current_state_tuple, current_total_volume_poured)]}, total volume poured: {current_total_volume_poured}")
            print(f"Search completed in {elapsed_time:.2f} ms")
            return cost_so_far[(current_state_tuple, current_total_volume_poured)]

        current_pitchers = [Pitcher(capacities[i], vol) for i, vol in enumerate(current_state_tuple)]
        successors = generate_successors(current_pitchers, current_total_volume_poured)

        for next_pitchers, next_total_volume_poured in successors:
            if next_total_volume_poured - target_volume > max_capacity:
                continue  # Skip adding this state to the open set as it exceeds the logical bound

            next_state_tuple = tuple(p.current_volume for p in next_pitchers)
            new_cost = cost_so_far[(current_state_tuple, current_total_volume_poured)] + sum(p.cost for p in next_pitchers)

            if (next_state_tuple, next_total_volume_poured) not in cost_so_far or new_cost < cost_so_far[(next_state_tuple, next_total_volume_poured)]:
                cost_so_far[(next_state_tuple, next_total_volume_poured)] = new_cost
                # Total volume
                # priority = new_cost + heuristic_volume_diff(next_state_tuple, target_volume)
                # Reservoir volume
                # priority = new_cost + heuristic_reservoir(next_total_volume_poured, target_volume)
                # Put modulo capacity priority here
                priority = new_cost + heuristic_modulo_capacity(capacities, target_volume)

                open_set.put((priority, (next_state_tuple, next_total_volume_poured)))
    
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    print(f"No solution found. Search completed in {elapsed_time:.2f} ms")
    return None


