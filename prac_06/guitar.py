"""
Guitar
Estimate: 30 minutes
Actual:    minutes
"""
class Guitar:
    def __init__(self, name, year, cost):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Convert a Guitar object into a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,}"