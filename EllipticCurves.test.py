import unittest
from Dot import Dot
from EllipticCurves import EllipticCurve
class TestDot(unittest.TestCase):
    def test_initialization(self):
        """Проверка инициализации точки."""
        dot = Dot(3, 5)
        self.assertEqual(dot.x, 3)
        self.assertEqual(dot.y, 5)

    def test_eqDot(self):
        """Проверка сравнения точек."""
        dot1 = Dot(3, 5)
        dot2 = Dot(3, 5)
        dot3 = Dot(1, 2)
        self.assertTrue(dot1.eqDot(dot2))  # Точки равны
        self.assertFalse(dot1.eqDot(dot3))  # Точки не равны

        # Проверка на сравнение с объектом другого типа
        with self.assertRaises(TypeError):
            dot1.eqDot("not a dot")

    def test_notDot(self):
        """Проверка неравенства точек."""
        dot1 = Dot(3, 5)
        dot2 = Dot(1, 2)
        self.assertTrue(dot1.notDot(dot2))  # Точки не равны
        self.assertFalse(dot1.notDot(Dot(3, 5)))  # Точки равны

    def test_stringDot(self):
        """Проверка строкового представления точки."""
        dot = Dot(3, 5)
        self.assertEqual(dot.stringDot(), "3, 5)")

    def test_hashDot(self):
        """Проверка хеширования точки."""
        dot1 = Dot(3, 5)
        dot2 = Dot(3, 5)
        dot3 = Dot(1, 2)
        self.assertEqual(dot1.hashDot(), dot2.hashDot())  # Хеши равны
        self.assertNotEqual(dot1.hashDot(), dot3.hashDot())  # Хеши не равны

    def test_copyDot(self):
        """Проверка копирования точки."""
        dot1 = Dot(3, 5)
        dot2 = dot1.copyDot()
        self.assertEqual(dot1.x, dot2.x)
        self.assertEqual(dot1.y, dot2.y)
        self.assertIsNot(dot1, dot2)  # Это разные объекты


class TestEllipticCurve(unittest.TestCase):
    def test_initialization(self):
        """Проверка инициализации эллиптической кривой."""
        curve = EllipticCurve(1, 2, 23)
        self.assertEqual(curve.a, 1)
        self.assertEqual(curve.b, 2)
        self.assertEqual(curve.p, 23)

    def test_invalid_parameters(self):
        """Проверка вызова исключения при недопустимых параметрах."""
        with self.assertRaises(ValueError):
            EllipticCurve(0, 0, 23)  # Не удовлетворяет условию -4a^3 - 27b^2 ≠ 0 (mod p)


if __name__ == "__main__":
    unittest.main()