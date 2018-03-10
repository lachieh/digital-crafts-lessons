number = int(raw_input("Enter a number: "))
last = number
divisor = 1

while (last > divisor):
    if(number % divisor == 0):
        last = number / divisor
        if (last == divisor):
            print divisor
        else:
            print divisor
            print last
    divisor += 1
