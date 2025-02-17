class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eqDot(self, other):
        if not isinstance(other, Dot):
            raise TypeError("Сравнение возможно только с объектами типа Dot (x, y))")
        return self.x == other.x and self.y == other.y

    def notDot(self, other):
        return not self.eqDot(other)

    def stringDot(self):
        return f"({self.x}, {self.y})"

    def hashDot(self):
        return hash((self.x, self.y))

    def copyDot(self):
        return Dot(self.x, self.y)

    def __eq__(self, other):
        return self.eqDot(other)

    def __str__(self):
        return self.stringDot()

    def __repr__(self):
        """Представление объекта для отладки."""
        return f"Dot(x={self.x}, y={self.y})"

    def __hash__(self):
        """Перегрузка оператора hash для поддержки хеширования."""
        return self.hashDot()