import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    # Тест на умножение с нулем
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    # Тест на вычисление площади квадрата
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

if __name__ == '__main__':
    unittest.main()