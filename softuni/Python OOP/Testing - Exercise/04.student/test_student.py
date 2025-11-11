from unittest import TestCase, main
from student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Ivan")

    def test_correct_init(self):
        self.assertEqual("Ivan", self.student.name)

    def test_enroll_course_in_courses_data_notes_are_updated_returns_string(self):
        self.student.courses = {"Python": []}

        expected_string = "Course already added. Notes have been updated."
        result = self.student.enroll("Python", ["note", "note_2"])

        self.assertEqual(expected_string, result)
        self.assertEqual(["note", "note_2"], self.student.courses["Python"])


if __name__ == "__main__":
    main()
