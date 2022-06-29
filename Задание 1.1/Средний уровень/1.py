import math


f = float(input("f = "))
y = float(input("y = "))
G = (math.e ** (2 * y) + math.sin(f)) / math.log(3.8 * y + f)
print("Ответ:", G)
