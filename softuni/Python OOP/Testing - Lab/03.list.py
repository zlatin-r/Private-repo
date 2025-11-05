from unittest import TestCase, main
from skeletons.class_int_list import IntegerList

class IntegerListTest(TestCase):
    def setUp(self):
        self.i_list = IntegerList(1, 2, 3, 4, 5.5, "hello")

    def test_add_integer_element_should_add_element_returns_list(self):
        expected = [1, 2, 3, 4, 6]
        
        self.i_list.add(6)

        result = self.i_list.get_data() 
        
        self.assertEqual(result, expected)

    def test_add_non_integer_el_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_with_correct_index(self):
        expected = [2, 3, 4]

        self.i_list.remove_index(0)

        result = self.i_list.get_data()

        self.assertEqual(result, expected)

    def test_remove_index_with_non_correct_index(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(8)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_init_should_take_only_integers_(self):
        expect = [1, 2, 3, 4]

        self.assertEqual(expect, self.i_list.get_data())

    def test_get_with_correct_index_should_return_element(self):
        expected = 2
        
        result = self.i_list.get(1)

        self.assertEqual(expected, result)

    def test_get_with_non_correct_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(8)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(8, 8)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_valid_index_and_integer_should_insert_element(self):
        self.i_list.insert(1, 10)
        expected = [1, 10, 2, 3, 4]
        self.assertEqual(self.i_list.get_data(), expected)

    def test_insert_with_non_integer_element_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(0, "string")

        self.assertEqual("Element is not Integer", str(ve.exception))
        
    def test_get_biggest_should_return_biggest_element(self):
        result = self.i_list.get_biggest()

        self.assertEqual(4, result)

    def test_get_index_should_return_element_index(self):
        result = self.i_list.get_index(1)

        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
