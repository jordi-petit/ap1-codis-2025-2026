# llegeix una hora i li suma un segon

import yogi

# lectura
h = yogi.read(int)
m = yogi.read(int)
s = yogi.read(int)

# càlcul
s = s + 1
if s == 60:
    s = 0
    m = m + 1
    if m == 60:
        m = 0
        h = h + 1
        if h == 24:
            h = 0

# escriptura
print(h, m, s)
