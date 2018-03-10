stringToReverse = raw_input("Reverse this: ")

wordLength = len(stringToReverse)

reversedWord = ''
for char in range(wordLength):
    reversedWord = reversedWord + stringToReverse[(wordLength - 1) - char]

print "reversed word: %s" % reversedWord
