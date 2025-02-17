from EllipticCurves import EllipticCurves
from Dot import Dot

def main():
    a = int(input("Введите параметр a для кривой: "))
    b = int(input("Введите параметр b для кривой: "))
    p = int(input("Введите параметр p для кривой: "))
    curve = EllipticCurves(a, b, p)

    while True:
        mode = int(input("Введите опцию exit/build curve/calculate a multiple point/subgroups of prime order [0/1/2/3]: "))
        if mode == 1:
            print("Количество точек: ", len(curve.find_dots()))
            print("Точки:")
            print(*curve.find_dots())
            orders = curve.find_orders()
            for dot, order in orders.items():
                print(f'Order({dot}) = {order}')
        elif mode == 2:
            x = int(input("Введите координату x точки: "))
            y = int(input("Введите координату y точки: "))
            k = int(input("Введите кратность точки: "))
            print(f'{k}P({x}; {y}) = {curve.calculate_multiplicity(Dot(x, y), k)}')
        elif mode == 3:
            curve.find_prime_subgroups()
        else:
            break

if __name__ == "__main__":
    main()