from yogi import scan

s = 0
x = scan(int)
while x != None:
    s = s + x
    x = scan(int)
print(s)
