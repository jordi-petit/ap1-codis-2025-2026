# calcula el màxim comú divisor de dos naturals (algorisme d'Euclides)
# precondició: els dos no poden ser zero

import yogi

a = yogi.read(int)
b = yogi.read(int)

while a != b:
    if a < b:
        b = b - a
    else:
        a = a - b
print(a)
