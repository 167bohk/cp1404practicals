class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""
    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine whether a ProgrammingLanguage is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Convert a ProgrammingLanguage object into a string."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"