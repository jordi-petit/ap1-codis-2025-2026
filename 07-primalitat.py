# diu si un nombre és primer
# ràpid!

import yogi

n = yogi.read(int)
i = 1
c = 0  # comptador de divisors
while i * i <= n and c <= 2:
    if n % i == 0:
        c = c + 2
    i = i + 1
if c > 2:
    print(n, "és compost")
else:
    print(n, "és primer")

# arregleu els casos n=0 i n=1, que no funcionen!
