def letter_histogram(word):
    tally = {}
    for char in word:
        if tally.get(char):
            tally[char] += 1
        else:
            tally[char] = 1
    return tally


print letter_histogram('banana')


def word_histogram(sentence):
    tally = {}
    wordsList = sentence.split()
    for word in wordsList:
        if tally.get(word):
            tally[word] += 1
        else:
            tally[word] = 1
    return tally


words = word_histogram(
    'the words and words for words then words thing a thing that thing best is best')
print words


def top_three(histogram):
    top_three_items = {}
    while len(top_three_items) < 3:
        highKey = ''
        highestValue = 0
        for key, value in histogram.items():
            if value > highestValue:
                highKey = key
                highestValue = value
        top_three_items[highKey] = histogram[highKey]
        del histogram[highKey]
    return top_three_items


print top_three(words)
