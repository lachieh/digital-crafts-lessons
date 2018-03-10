height = 4
base = height * 2 - 1

for row in range(1, height + 1):
    spaces = height - row
    print " " * spaces + "*" * (row * 2 - 1)
