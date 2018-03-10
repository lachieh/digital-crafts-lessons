number = int(raw_input("Enter a number: "))
last = number
divisor = 1

left = []
right = []

while (last > divisor):
    if(number % divisor == 0):
        last = number / divisor
        if (last == divisor):
            left.append(divisor)
        else:
            left.append(divisor)
            right.insert(0,last)
    divisor += 1
print left + right
