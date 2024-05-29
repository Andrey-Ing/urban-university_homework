from main import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student('III')

    def test_walk_1(self):
        for _ in range(10):
            self.student.walk()
        self.assertEqual(self.student.distance, 50, 'Дистанции не равны '
                                                    '[дистанция человека(объекта)] != 50')

    def test_run_1(self):
        for _ in range(10):
            self.student.run()
        self.assertEqual(self.student.distance, 100, 'Дистанции не равны '
                                                     '[дистанция человека(объекта)] != 100')

    def test_run_walk_1(self):
        student_dummy = Student('KKK')
        for _ in range(1000):
            self.student.walk()
            student_dummy.run()
        self.assertLess(self.student.distance, student_dummy.distance, '[бегущий человек] должен '
                                                                       'преодолеть дистанцию больше, '
                                                                       'чем [идущий человек].')


if __name__ == '__main__':
    unittest.main()
