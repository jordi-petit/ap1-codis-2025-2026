# calcula el màxim comú divisor de dos naturals (algorisme d'Euclides eficient)
# precondició: els dos no poden ser zero

import yogi

a = yogi.read(int)
b = yogi.read(int)

while b != 0:
    r = a % b
    a = b
    b = r
print(a)
