from unittest import TestCase, main
from hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ivan", 10, 100, 10)
        self.enemy_hero = Hero("enemy", 10, 100, 10)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_with_correct_name_and_hero_and_enemy_health_more_than_0_hero_wins(self):
        self.enemy_hero.level = 9
        self.enemy_hero.damage = 5

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(60, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_with_correct_name_hero_and_enemy_health_more_than_0_hero_lose(self):
        self.hero.damage = 5
        self.enemy_hero.level = 11
        self.enemy_hero.damage = 15

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(12, self.enemy_hero.level)
        self.assertEqual(55, self.enemy_hero.health)
        self.assertEqual(20, self.enemy_hero.damage)

    def test_battle_with_correct_name_hero_and_enemy_health_more_than_0_battle_draw(self):
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("Draw", result)

    def test_battle_with_same_hero_and_enemy_hero_names_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_correct_name_hero_health_less_than_0_raises_exception(self):
        self.hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_correct_name_enemy_health_less_than_0_raises_exception(self):
        self.enemy_hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight enemy. He needs to rest", str(ex.exception))

    def test_correct__str__(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_result, str(self.hero))


if __name__ == "__main__":
    main()
