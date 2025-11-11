from unittest import TestCase, main
from hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ivan", 10, 100, 10)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_with_correct_name_and_hero_and_enemy_health_more_than_0_hero_wins(self):
        enemy_hero = Hero("enemy", 9, 100, 5)

        result = self.hero.battle(enemy_hero)

        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(60, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_with_correct_name_hero_and_enemy_health_more_than_0_hero_lose(self):
        self.hero.damage = 5
        enemy_hero = Hero("enemy", 11, 100, 15)

        result = self.hero.battle(enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(12, enemy_hero.level)
        self.assertEqual(55, enemy_hero.health)
        self.assertEqual(20, enemy_hero.damage)

    def test_battle_with_correct_name_hero_and_enemy_health_more_than_0_battle_draw(self):
        enemy_hero = Hero("enemy", 10, 100, 10)

        result = self.hero.battle(enemy_hero)

        self.assertEqual("Draw", result)

    def test_battle_with_same_hero_and_enemy_hero_names_raises_exception(self):
        enemy_hero = Hero("Ivan", 10, 100, 10)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself")


if __name__ == "__main__":
    main()
