import datetime


class Project:
    """Represent information about a project."""

    def __init__(self, name="", start_date=datetime.datetime.today().date(), priority=0, cost_estimate=0.0,
                 completion_percentage=0):
        """Initialize a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a Project object in string format."""
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Determine whether a Project has less priority than another one."""
        return self.priority < other.priority

    def is_recent(self, threshold=datetime.datetime.today().date()):
        """Determine whether a project is recent, depending on the threshold given by user."""
        return self.start_date >= threshold

