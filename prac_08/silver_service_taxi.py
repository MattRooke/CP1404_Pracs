from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a taxi that includes fanciness scale."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.00):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance and flagfall."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
