word = raw_input('The word: ').upper()

result = ''

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

for char in word:
    result_char = char
    if result_char == 'A':
        result_char = '4'
    if result_char == 'E':
        result_char = '3'
    if result_char == 'G':
        result_char = '6'
    if result_char == 'I':
        result_char = '1'
    if result_char == 'O':
        result_char = '0'
    if result_char == 'S':
        result_char = '5'
    if result_char == 'T':
        result_char = '7'
    result = result + result_char


print result
