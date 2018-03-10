from turtle import *


def drawCircle(size=100):
    circle(size)


def drawSquare(size=100):
    for i in range(4):
        forward(size)
        left(90)


def drawTriangle(size=100):
    for i in range(3):
        forward(size)
        left(120)


if __name__ == "__main__":
    drawSquare()

    up()
    forward(200)
    down()

    drawSquare()
