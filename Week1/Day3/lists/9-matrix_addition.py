listA = [[2, 3], [6, 3]]
listB = [[1, 9], [4, 5]]

# make a container to store the new lists in
resultList = []

# for each list inside listA, make a range of its length
for indexA in range(len(listA)):
    # create a container to store the new lists
    innerResultList = []
    # for each integer inside the current list
    for indexB in range(len(listA[indexA])):
        # calculate the result from the appropriate location in the 2 dimensional list
        result = listA[indexA][indexB] + listB[indexA][indexB]
        # add the result to our inner result container
        innerResultList.append(result)
    # add our result list to the main result list
    resultList.append(innerResultList)

print resultList  # print the multiplied numbers
