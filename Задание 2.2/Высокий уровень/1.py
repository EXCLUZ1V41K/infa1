import math


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
if a == 0:
    print("Решения нет")
else:
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 =", x1, "x2 = ", x2)
    elif discr == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:
        print("Корней нет")
