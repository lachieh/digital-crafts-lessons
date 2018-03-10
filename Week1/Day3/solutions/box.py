width = int(raw_input('Width? '))
height = int(raw_input('Height? '))

# draw the top border
print '*' * width

# draw the middle
num_spaces = width - 2
spaces = ' ' * num_spaces
for i in range(height - 2):
    print '*' + spaces + '*'

# draw the bottom border
print '*' * width
