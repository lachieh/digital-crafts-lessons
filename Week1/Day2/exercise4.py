total = int(raw_input("What is the total? "))
serviceValue = raw_input("What was the service like? ")
acceptedServiceValues = ["good", "fair", "bad"]

while serviceValue not in acceptedServiceValues:
    print "Not a valid service level. Type good, fair, or bad."
    serviceValue = raw_input("What was the service like? ")

if serviceValue == "good":
    percentage = 20
elif serviceValue == "fair":
    percentage = 15
elif serviceValue == "bad":
    percentage = 10

split = int(raw_input("How many people to split the bill by? "))
tip = (total / 100 * percentage) / split
print "The tip is $%s" % tip
