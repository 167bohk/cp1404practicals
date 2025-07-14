
class Guitar:
    """Represent a Guitar object."""

    VINTAGE_THRESHOLD = 50

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Convert a Guitar object into a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,}"

    def get_age(self, current_year):
        """Returns how old the guitar is in years"""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Determine whether a Guitar is vintage."""
        return self.get_age(current_year) >= Guitar.VINTAGE_THRESHOLD

    def __lt__(self, other):
        """Determine whether a Guitar object is less than another Guitar object."""
        return self.year < other.year
