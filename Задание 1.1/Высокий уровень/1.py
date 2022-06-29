import math


a = float(input("a = "))
x = float(input("x = "))
c = float(input("c = "))
L = (math.sqrt(math.e ** x - math.cos((x ** 2) * (a ** 5)) ** 4) + math.atan(a - x ** 5) ** 4) / math.e * math.sqrt(abs(a + x * c ** 4))
print("Ответ:", L)
