numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

positives = []  # prepare a container variable to store the postive numbers number
for number in numbers:  # for each number in the list
    if number >= 0:  # if the current number is greater than or equal to zero
        positives.append(number)  # add the positive numbers to our container

print positives  # print the smallest number
