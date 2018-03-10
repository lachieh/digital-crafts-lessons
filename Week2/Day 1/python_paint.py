def drawSquare(width, height):
    print '*' * width
    num_spaces = width - 2
    spaces = ' ' * num_spaces
    for i in range(height - 2):
        print '*' + spaces + '*'
    print '*' * width


def drawTriangle(height):
    base = height * 2 - 1
    for row in range(1, height + 1):
        spaces = height - row
        print " " * spaces + "*" * (row * 2 - 1)


def drawBox(width, height):
    for row in range(height):
        if row == 0:
            print "*" * width
        elif row == height - 1:
            print "*" * width
        else:
            spaces = width - 2
            print "*" + " " * spaces + "*"


if __name__ == '__main__':
    height = int(raw_input("what's the height? "))
    drawSquare(5, height)
    drawTriangle(height)
    drawBox(10, height)
