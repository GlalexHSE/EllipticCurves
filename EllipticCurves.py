from ArithmeticMod import ArithmeticMod
from Dot import Dot
import math
import random

class EllipticCurves:
    def __init__(self, a, b, p):
        if (-4 * a**3 - 27 * b**2) % p == 0:
            raise ValueError("Параметры должны удовлетворять условию: -4a^3-27b^2 ≠ 0 (mod p)")
        self.p = p
        self.a = ArithmeticMod(a, p)
        self.b = ArithmeticMod(b, p)
        self.dots = []

    def is_on_curve(self, dot):
        """Проверяет, лежит ли точка на кривой."""
        if dot is None:
            return True  # Бесконечно удалённая точка
        x = ArithmeticMod(dot.x, self.p)
        y = ArithmeticMod(dot.y, self.p)
        return y**2 == x**3 + self.a * x + self.b

    def add_dots(self, p1, p2):
        """Сложение двух точек на эллиптической кривой."""
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        # Преобразуем координаты точек в ArithmeticMod
        x1 = ArithmeticMod(p1.x, self.p)
        y1 = ArithmeticMod(p1.y, self.p)
        x2 = ArithmeticMod(p2.x, self.p)
        y2 = ArithmeticMod(p2.y, self.p)

        if p1 == p2:
            if y1.value == 0:
                return None  # Бесконечно удалённая точка
            # Удвоение точки
            s = (ArithmeticMod(3, self.p) * x1**2 + self.a) / (ArithmeticMod(2, self.p) * y1)
        else:
            if x1 == x2:
                return None  # Бесконечно удалённая точка
            # Сложение разных точек
            s = (y2 - y1) / (x2 - x1)

        x3 = s**2 - x1 - x2
        y3 = s * (x1 - x3) - y1
        return Dot(int(x3), int(y3))

    def find_dots(self):
        """Находит все точки на эллиптической кривой."""
        if self.dots:
            return self.dots
        for x in range(self.p):
            xm = ArithmeticMod(x, self.p)
            y_squared = xm**3 + self.a * xm + self.b
            if y_squared.value == 0:
                self.dots.append(Dot(x, 0))
            elif self.is_quadratic_residue(y_squared.value):
                y = self.sqrt_mod(y_squared.value)
                self.dots.append(Dot(x, y))
                self.dots.append(Dot(x, self.p - y))
        self.dots.append(None)  # Бесконечно удалённая точка
        return self.dots

    def is_quadratic_residue(self, a):
        """Проверяет, является ли a квадратичным вычетом по модулю p."""
        return pow(a, (self.p - 1) // 2, self.p) == 1

    def sqrt_mod(self, a):
        """Находит квадратный корень по модулю p (алгоритм Тонелли-Шэнкса)."""
        if a == 0:
            return 0
        if self.p == 2:
            return a
        if self.p % 4 == 3:
            return pow(a, (self.p + 1) // 4, self.p)

        # Алгоритм Тонелли-Шэнкса для p % 4 == 1
        Q = self.p - 1
        S = 0
        while Q % 2 == 0:
            Q //= 2
            S += 1

        z = 2
        while self.is_quadratic_residue(z):
            z += 1

        c = pow(z, Q, self.p)
        x = pow(a, (Q + 1) // 2, self.p)
        t = pow(a, Q, self.p)
        m = S
        while t != 1:
            i = 0
            temp = t
            while temp != 1 and i < m:
                temp = pow(temp, 2, self.p)
                i += 1
            b = pow(c, 2 ** (m - i - 1), self.p)
            x = (x * b) % self.p
            t = (t * b * b) % self.p
            c = (b * b) % self.p
            m = i
        return x

    def find_orders(self):
        """Находит порядок каждой точки на кривой."""
        orders = {}
        for dot in self.find_dots():
            if dot is None:
                orders[None] = 1
                continue
            current = dot
            count = 1
            while current is not None:
                current = self.add_dots(current, dot)
                count += 1
            orders[dot] = count
        return orders

    def calculate_multiplicity(self, dot, k):
        """Вычисляет точку kP."""
        result = None
        for _ in range(k):
            result = self.add_dots(result, dot)
        return result

    def find_prime_subgroups(self):
        """Находит подгруппы простого порядка."""
        orders = self.find_orders()
        for dot, order in orders.items():
            if self.is_prime(order):
                print(f"Подгруппа с порядком {order}:")
                current = dot
                while current is not None:
                    print(current)
                    current = self.add_dots(current, dot)
                print("None")  # Добавляем бесконечно удалённую точку

    def is_prime(self, n):
        """Проверяет, является ли число простым (тест Ферма)."""
        if n < 2:
            return False
        if n == 2:  # 2 — наименьшее простое число
            return True
        for _ in range(10):  # 10 итераций для повышения точности
            a = random.randint(2, n - 1)
            if pow(a, n - 1, n) != 1:
                return False
        return True