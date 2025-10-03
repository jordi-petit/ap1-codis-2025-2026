from yogi import read

s = 0
x = read(int)
while x != -1:
    s = s + x
    x = read(int)
print(s)
