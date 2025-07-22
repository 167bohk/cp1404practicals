from prac_09.musician import Musician
class Band:
    """Band class"""
    def __init__(self, name):
        """Initialize a Band object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string format band name and its musicians."""
        return f"{self.name} ({", ".join([f"{musician.__str__()}" for musician in self.musicians])})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)


    def play(self):
        """Return a string showing the musicians of the band playing their first (or no) instrument."""
        if not self.musicians:
            return f"{self.name} needs a musician!"
        return f"{"\n".join([musician.play() for musician in self.musicians])}"
