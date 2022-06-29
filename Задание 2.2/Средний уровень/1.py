import math


a = float(input("a = "))
b = float(input("b = "))
while a >= 0 and b >= 0:
    res1 = (a + b) / 2
    print("Ответ:", res1)
    break
res2 = math.sqrt(abs(a + b))
print("Ответ:", res2)
