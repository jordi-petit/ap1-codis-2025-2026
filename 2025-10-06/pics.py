from yogi import tokens, scan

"""Comptar nombre de cims."""


cims = 0
a = scan(int)
if a != None:
    b = scan(int)
    if b != None:
        for c in tokens(int):
            if a < b > c:
                cims = cims + 1
            a = b
            b = c
print(cims)
