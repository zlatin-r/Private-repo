from unittest import TestCase, main
from mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.animal = Mammal("Gosho", "dog", "bau")

    def test_correct_init(self):
        self.assertEqual("Gosho", self.animal.name)
        self.assertEqual("dog", self.animal.type)
        self.assertEqual("bau", self.animal.sound)

    def test_make_sound_should_return_string(self):
        self.assertEqual("Gosho makes bau", self.animal.make_sound())

    def test_get_kingdom_should_return_string_kingdom(self):
        self.assertEqual("animals", self.animal.get_kingdom())

    def test_info_should_return_string_name_and_type(self):
        self.assertEqual("Gosho is of type dog", self.animal.info())


if __name__ == "__main__":
    main()
    