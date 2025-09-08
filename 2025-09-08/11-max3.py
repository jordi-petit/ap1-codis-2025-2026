# programa que llegeix tres nombres i escriu el seu màxim

x = int(input())
y = int(input())
z = int(input())

if x >= y:
    if x >= z:
        m = x
    else:
        m = z
else:
    if y >= z:
        m = y
    else:
        m = z

print(m)
