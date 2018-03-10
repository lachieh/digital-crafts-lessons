numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

largest = 0  # create an empty placeholder
for number in numbers:  # for each number in the numbers list
    if number > largest:  # if the current number is larger than the previous
        largest = number  # then set the current number into our container

print largest  # print the largest number
