# pograma que escriu les taules de multiplicar (amb un for)

for i in range(1, 11):
    print("Taula del", i)
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print()
