a = float(input("a = "))
b = float(input("b = "))
sk = a ** 2 + b ** 2
ks = (a + b) ** 2
if sk > ks:
    print("Сумма квадратов больше")
elif sk < ks:
    print("Квадрат суммы больше")
else:
    print("Они равны")
