from unittest import TestCase, main
from  skeletons.class_worker import Worker

class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Todor", 20_200, 200)

    def test_correct_init(self):
        self.assertEqual("Todor", self.worker.name)
        self.assertEqual(20_200, self.worker.salary)
        self.assertEqual(200, self.worker.energy)

    def test_if_energy_is_incremented_after_rest_method_is_called(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(self.worker.energy, expected_energy)

    def test_if_exeption_raised_when_worker_with_0_or_less_energy_works(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_money_increaced_after_work_method(self):
        expected_money = self.worker.money + 20_200

        self.worker.work()

        self.assertEqual(self.worker.money, expected_money)

    def test_if_energy_decreaced_after_work_method(self):
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(self.worker.energy, expected_energy)

    def test_if_get_info_method_returns_correct_string(self):
        self.worker.money = 1000
        self.worker.name = "Ivan"

        expected_string = "Ivan has saved 1000 money."
        result = self.worker.get_info()

        self.assertEqual(result, expected_string)

if __name__ == '__main__':
    main()
