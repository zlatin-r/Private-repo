from unittest import TestCase, main
from vehicle import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100.0, 200.0)


if __name__ == "__main__":
    main()
