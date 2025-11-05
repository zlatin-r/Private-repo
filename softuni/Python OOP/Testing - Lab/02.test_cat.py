from unittest import TestCase, main
from skeletons.class_cat import Cat

class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_if_size_increased_after_eating(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_if_fed_after_eating(self):
        self.cat.fed = False

        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_cant_eat_after_fed_is_true(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cant_fall_sleep_if_not_fed(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_if_sleepy_after_sleeping(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
