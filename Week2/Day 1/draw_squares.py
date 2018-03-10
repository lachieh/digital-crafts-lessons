from turtle import *
from shapes import *

coord_list = [
    (-100, 100, 50),
    (100, 100, 100),
    (100, -100, 200),
    (-100, -100, 5)
]

for coord in coord_list:
    up()
    home()
    x, y, size = coord
    setheading(270)
    forward(x)
    setheading(0)
    forward(y)
    down()
    drawSquare(size)

mainloop()
