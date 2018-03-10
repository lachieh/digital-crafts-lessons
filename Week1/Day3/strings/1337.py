stringToLeet = raw_input("leet this: ").upper()

# This section makes the word 1337
stringToLeet = stringToLeet.replace("A", "4")
stringToLeet = stringToLeet.replace("E", "3")
stringToLeet = stringToLeet.replace("G", "6")
stringToLeet = stringToLeet.replace("I", "1")
stringToLeet = stringToLeet.replace("O", "0")
stringToLeet = stringToLeet.replace("S", "5")
stringToLeet = stringToLeet.replace("T", "7")

print stringToLeet
