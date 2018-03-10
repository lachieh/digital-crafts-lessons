numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]
multiplier = 3  # need a number to multiply by

mulitpliedNumbers = []  # make a container to store the multiplied values in
# make a 'range' equal to the length of the list of number, then for each value in that array
for index in range(len(numbers)):
    # append the multiplied number at the current index to out container
    mulitpliedNumbers.append(numbers[index] * multiplier)

print mulitpliedNumbers  # print the multiplied numbers
