numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

total = 0  # set a container variable to store the total in
for number in numbers:  # for each number in the numbers list
    total += number  # add the current number to the existing total
    # note here the use of the '+=' as a method of adding the RHS to the LHS

print total  # print the total number
