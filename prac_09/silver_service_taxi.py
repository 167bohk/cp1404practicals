from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that have flagfalls and the charging rate depends on the fanciness."""
    flagfall = 4.50
    def __init__(self, fanciness:float, **kwargs):
        """Initialize a SilverServiceTaxi object."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall


    def __str__(self):
        """Return a string like a Car but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"
