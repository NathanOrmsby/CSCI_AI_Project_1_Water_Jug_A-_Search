from pitcher import Pitcher

total_volume_poured = 0

def initialize_state(capacities):
    # Initialize pitchers based on capacities
    pitchers = [Pitcher(capacity) for capacity in capacities]
    return pitchers

def generate_successors(pitchers, total_volume_poured):
    successors = []
    for i, pitcher in enumerate(pitchers):
        # Fill action
        # print("In generate successors\n\n")
        # print(type(pitcher))
        # print(f"pitcher volume: {pitcher.current_volume}, type: {type(pitcher.current_volume)}")
        if pitcher.current_volume < pitcher.capacity:
            new_pitchers = [Pitcher(p.capacity, p.current_volume) for p in pitchers]
            new_pitchers[i].fill()
            # When filling, total_volume_poured does not change
            successors.append((new_pitchers, total_volume_poured))
        
        # Empty action
        if pitcher.current_volume > 0:
            new_pitchers = [Pitcher(p.capacity, p.current_volume) for p in pitchers]
            # Update the total volume poured as this pitcher is emptied
            updated_total_volume_poured = total_volume_poured + new_pitchers[i].current_volume
            new_pitchers[i].empty()
            successors.append((new_pitchers, updated_total_volume_poured))
        
        # Pour actions
        for j, target_pitcher in enumerate(pitchers):
            if i != j and pitcher.current_volume > 0 and target_pitcher.current_volume < target_pitcher.capacity:
                new_pitchers = [Pitcher(p.capacity, p.current_volume) for p in pitchers]
                # Calculate the pour volume before actually pouring
                pour_volume = min(pitcher.current_volume, target_pitcher.capacity - target_pitcher.current_volume)
                new_pitchers[i].pour_into(new_pitchers[j])
                # Pouring does not change the total volume poured into the infinite capacity
                successors.append((new_pitchers, total_volume_poured))
    
    return successors




def calculate_state_cost(pitchers):
    """Calculate the total cost of a state."""
    return sum(p.cost for p in pitchers)