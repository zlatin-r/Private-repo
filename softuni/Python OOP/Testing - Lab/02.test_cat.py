from unittest import TestCase, main
from skeletons.class_test_cat import Cat

class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_if_cat_size_increased_after_eating(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_cant_eat_after_fed_is_true(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    

if __name__ == "__main__":
    main()
