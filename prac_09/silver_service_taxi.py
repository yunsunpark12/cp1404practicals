from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):

    FLAGFALL = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.fare = self.price_per_km * self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return round((self.fare * self.current_fare_distance) + self.FLAGFALL, 1)

    def __str__(self):
        super(SilverServiceTaxi, self).__str__()
        return "{}, fuel={:.1f}, odo={:.1f}, {:.1f}km on current fare, ${}/km plus flagfall of ${:.2f}".format(
            self.name, self.fuel, self.odometer,
            self.current_fare_distance,
            self.fare, self.FLAGFALL)


