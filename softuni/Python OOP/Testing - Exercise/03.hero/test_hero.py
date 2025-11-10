from unittest import TestCase, main
from hero import Hero

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ivan", 10, 100, 50)

    def test_correct_init(self):
        pass


if __name__ == "__main__":
    main()
