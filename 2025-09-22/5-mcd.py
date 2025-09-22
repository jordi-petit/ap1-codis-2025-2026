# calcula el màxim comú divisor de dos naturals
# precondició: els dos no poden ser zero

import yogi

a = yogi.read(int)
b = yogi.read(int)

if a < b:
    d = a
else:
    d = b
while not (a % d == 0 and b % d == 0):
    d = d - 1

print(d)
