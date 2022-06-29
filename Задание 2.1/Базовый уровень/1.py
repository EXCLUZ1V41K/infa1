a = 1
b = 0
c = 0
print((a or not a and b) or c)
print(not a or a and (b or c))
print((a or b and not c) and c)
