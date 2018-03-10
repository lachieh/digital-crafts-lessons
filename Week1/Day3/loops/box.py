width = int(raw_input("How wide is the box? "))
height = int(raw_input("How tall is the box? "))

for row in range(height):
    if row == 0:
        print "*" * width
    elif row == height - 1:
        print "*" * width
    else:
        spaces = width - 2
        print "*" + " " * spaces + "*"
