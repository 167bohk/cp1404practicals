class Monitor:
    """Represent"""

    def __init__(self, model, width, height):
        """Initialize a Monitor object."""
        self.model = model
        self.width = width
        self.height = height

    def get_resolution(self):
        """Get resolution(in tuple) for a Monitor object."""
        return tuple((self.width, self.height))

    def get_total_pixels(self):
        """Get total pixels for a Monitor object."""
        return self.width * self.height


    def __eq__(self, other):
        """Determine whether two Monitor objects are same."""
        return self.width == other.width and self.height == other.height


def run_tests():
    """Run simple tests on Monitor class."""
    monitor1 = Monitor("apple", 2560, 1660)
    monitor2 = Monitor("dell", 2560, 1660)
    monitor3 = Monitor("lenovo", 1920, 1080)
    print(monitor1.get_resolution())
    print(monitor1.get_total_pixels())
    print(monitor2 == monitor3)
    assert monitor1 == monitor2


if __name__ == "__main__":
    run_tests()

