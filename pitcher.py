class Pitcher:
    def __init__(self, capacity, current_volume=0):
        self.capacity = capacity
        self.current_volume = current_volume
        self.cost = 0

    def fill(self):
        """Fill the pitcher to its capacity from the infinite source."""
        self.current_volume = self.capacity
        self.cost += 1  # Increment cost by 1 for filling

    def empty(self):
        """Empty the pitcher back into the infinite source."""
        self.current_volume = 0
        self.cost += 1  # Increment cost by 1 for filling

    def pour_into(self, other_pitcher):
        """Pour water from this pitcher into another pitcher."""
        available_space = other_pitcher.capacity - other_pitcher.current_volume
        amount_poured = min(self.current_volume, available_space)
        self.current_volume -= amount_poured
        other_pitcher.current_volume += amount_poured
        self.cost += 1  # Increment cost by 1 for filling

    def __repr__(self):
        return f"Pitcher(capacity={self.capacity}, current_volume={self.current_volume})"