word = raw_input('sentence: ')

long_vowels = ['oo', 'ee', 'aa', 'ii', 'uu']

result = ''
for index in range(len(word)):                 # [0,1,2,3,4,5]
    twoletters = word[index:index+2]
    if twoletters in long_vowels:
        result += word[index] * 4
    else:
        result += word[index]

print result
