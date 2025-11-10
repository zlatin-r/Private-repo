from unittest import TestCase, main
from skeletons.class_car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Audi", "A4", 15, 100)

    def test_correct_init(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("A4", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_value(self):
        self.car.make = "Lada"
        self.assertEqual("Lada", self.car.make)

    def test_make_without_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_value(self):
        self.car.model = "Samara"
        self.assertEqual("Samara", self.car.model)

    def test_model_without_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_value_more_than_0(self):
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)

    
    def test_fuel_consumption_with_value_equal_to_0(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_value_less_than_0_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_correct_value_more_than_0(self):
        self.car.fuel_capacity = 1
        self.assertEqual(1, self.car.fuel_capacity)

    def test_fuel_capacity_with_value_equal_to_0_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_value_less_than_0_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_correct_value_more_than_0(self):
        self.car.fuel_amount = 1
        self.assertEqual(1, self.car.fuel_amount)

    def test_fuel_amount_with_value_equal_to_0(self):
        self.car.fuel_amount = 0
        self.assertEqual(0, self.car.fuel_amount)

    def test_fuel_amount_with_value_less_than_0_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_value_more_than_0_fuel_amount_less_than_capacity(self):
        self.car.refuel(50)
        self.assertEqual(50, self.car.fuel_amount)

    def test_refuel_with_value_more_than_0_fuel_amount_more_than_capacity(self):
        self.car.refuel(120)
        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_refuel_with_value_less_than_0_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_with_distance_less_than_fuel_needed_amount_reduced(self):
        self.car.refuel(1000)
        self.car.drive(10)
        self.assertEqual(98.5, self.car.fuel_amount)

    def test_drive_without_needed_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
