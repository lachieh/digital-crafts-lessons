numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

smallest = 0  # prepare a container variable to store the smallest number
for number in numbers:  # for each number in the list
    if number < smallest:  # if the current number is less than the previous smallest
        smallest = number  # smallest is no equal to the current number

print smallest  # print the smallest number
