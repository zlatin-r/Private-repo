from unittest import TestCase, main
from vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        expected = self.vehicle.fuel - (self.vehicle.fuel_consumption * 10)
        self.vehicle.drive(10)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_drive_with_not_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_fuel_less_than_capacity(self):
        self.vehicle.fuel = 50
        self.vehicle.capacity = 100

        self.vehicle.refuel(20)

        self.assertEqual(70, self.vehicle.fuel)

    def test_refuel_with_fuel_more_than_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(120)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method_message_returns_string(self):
        expected = "The vehicle has 200 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, self.vehicle.__str__())

if __name__ == "__main__":
    main()
