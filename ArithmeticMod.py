class ArithmeticMod:
    """
    Класс для работы с целыми числами по модулю m.
    Поддерживает основные арифметические операции и нахождение обратного элемента.
    """

    def __init__(self, value: int, modulus: int):
        """
        Инициализирует объект ArithmeticMod.
        
        :param value: Значение числа.
        :param modulus: Модуль.
        """
        if modulus <= 0:
            raise ValueError("Модуль должен быть положительным числом.")
        self.modulus = modulus
        self.value = value % modulus  # Приводим значение по модулю

    def __int__(self):
        """Возвращает значение числа."""
        return self.value

    def __add__(self, other):
        """Сложение двух чисел по модулю."""
        if isinstance(other, ArithmeticMod):
            if self.modulus != other.modulus:
                raise ValueError("Модули чисел должны совпадать.")
            return ArithmeticMod(self.value + other.value, self.modulus)
        elif isinstance(other, int):
            return ArithmeticMod(self.value + other, self.modulus)
        else:
            raise TypeError("Неподдерживаемый тип операнда.")

    def __sub__(self, other):
        """Вычитание двух чисел по модулю."""
        if isinstance(other, ArithmeticMod):
            if self.modulus != other.modulus:
                raise ValueError("Модули чисел должны совпадать.")
            return ArithmeticMod(self.value - other.value, self.modulus)
        elif isinstance(other, int):
            return ArithmeticMod(self.value - other, self.modulus)
        else:
            raise TypeError("Неподдерживаемый тип операнда.")

    def __mul__(self, other):
        """Умножение двух чисел по модулю."""
        if isinstance(other, ArithmeticMod):
            if self.modulus != other.modulus:
                raise ValueError("Модули чисел должны совпадать.")
            return ArithmeticMod(self.value * other.value, self.modulus)
        elif isinstance(other, int):
            return ArithmeticMod(self.value * other, self.modulus)
        else:
            raise TypeError("Неподдерживаемый тип операнда.")

    def __truediv__(self, other):
        """Деление двух чисел по модулю (умножение на обратный элемент)."""
        if isinstance(other, ArithmeticMod):
            if self.modulus != other.modulus:
                raise ValueError("Модули чисел должны совпадать.")
            return self * other.inverse()
        elif isinstance(other, int):
            return self * ArithmeticMod(other, self.modulus).inverse()
        else:
            raise TypeError("Неподдерживаемый тип операнда.")

    def __pow__(self, exponent: int):
        """Возведение в степень по модулю."""
        if not isinstance(exponent, int):
            raise TypeError("Степень должна быть целым числом.")
        return ArithmeticMod(pow(self.value, exponent, self.modulus), self.modulus)

    def inverse(self):
        """Находит обратный элемент по модулю."""
        def extended_gcd(a, b):
            """Расширенный алгоритм Евклида для нахождения НОД и коэффициентов."""
            if b == 0:
                return a, 1, 0
            else:
                gcd, x, y = extended_gcd(b, a % b)
                return gcd, y, x - (a // b) * y

        gcd, x, _ = extended_gcd(self.value, self.modulus)
        if gcd != 1:
            raise ValueError("Обратный элемент не существует, так как НОД != 1.")
        return ArithmeticMod(x % self.modulus, self.modulus)

    def __eq__(self, other):
        """Проверка на равенство."""
        if isinstance(other, ArithmeticMod):
            return self.value == other.value and self.modulus == other.modulus
        elif isinstance(other, int):
            return self.value == other % self.modulus
        else:
            return False

    def __ne__(self, other):
        """Проверка на неравенство."""
        return not self.__eq__(other)

    def __str__(self):
        """Строковое представление числа."""
        return f"{self.value} (mod {self.modulus})"

    def __repr__(self):
        """Представление объекта для отладки."""
        return f"ArithmeticMod(value={self.value}, modulus={self.modulus})"

    def __neg__(self):
        """Возвращает отрицательное значение числа по модулю."""
        return ArithmeticMod(-self.value, self.modulus)

    def __lt__(self, other):
        """Сравнение: меньше."""
        if isinstance(other, ArithmeticMod):
            if self.modulus != other.modulus:
                raise ValueError("Модули чисел должны совпадать.")
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other % self.modulus
        else:
            raise TypeError("Неподдерживаемый тип операнда.")

    def __le__(self, other):
        """Сравнение: меньше или равно."""
        if isinstance(other, ArithmeticMod):
            if self.modulus != other.modulus:
                raise ValueError("Модули чисел должны совпадать.")
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other % self.modulus
        else:
            raise TypeError("Неподдерживаемый тип операнда.")

    def __gt__(self, other):
        """Сравнение: больше."""
        if isinstance(other, ArithmeticMod):
            if self.modulus != other.modulus:
                raise ValueError("Модули чисел должны совпадать.")
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other % self.modulus
        else:
            raise TypeError("Неподдерживаемый тип операнда.")

    def __ge__(self, other):
        """Сравнение: больше или равно."""
        if isinstance(other, ArithmeticMod):
            if self.modulus != other.modulus:
                raise ValueError("Модули чисел должны совпадать.")
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other % self.modulus
        else:
            raise TypeError("Неподдерживаемый тип операнда.")