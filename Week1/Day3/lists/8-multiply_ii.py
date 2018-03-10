numbers = [2, 3, 6, -10]
numbers2 = [0, 9, 32, 5]

# make a container to store the multiplied values in
mulitpliedNumbers = []
# make a 'range' equal to the length of the list of number, then for each value in that array
for index in range(len(numbers)):
    # multiply the number at the current index with the number at the same index in numbers2
    value = numbers[index] * numbers2[index]
    # append the multiplied number to our container
    mulitpliedNumbers.append(value)

print mulitpliedNumbers  # print the multiplied numbers
