class EllipticCurve:
    def __init__(self, a, b, p):
        if (-4 * a**3 - 27 * b**2) % p == 0:
            raise ValueError("Параметры должны удовлетворять условию: -4a^3-27b^2 ≠ 0 (mod p)")
        self.p = p
        self.a = a % p
        self.b = b % p
        