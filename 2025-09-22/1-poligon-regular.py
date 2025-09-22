# programa que pinta un poligon regular

import yogi
import turtle

mida = yogi.read(int)
costats = yogi.read(int)

i = 1
while i <= costats:
    turtle.forward(mida)
    turtle.right(360 / costats)
    i = i + 1

turtle.done()
