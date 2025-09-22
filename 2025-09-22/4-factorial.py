# calcula el factorial d'un nombre natural

import yogi

n = yogi.read(int)

f = 1
for i in range(2, n + 1):
    f = f * i

print(f)
