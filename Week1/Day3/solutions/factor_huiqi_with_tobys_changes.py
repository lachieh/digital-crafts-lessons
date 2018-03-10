import math
n = int(raw_input("what's the number?"))

for i in range(1, int(math.sqrt(n))):
   if n % i == 0:
       little_brother = n/i
       big_brother = n / little_brother
       if little_brother == big_brother:
           print little_brother
       else:
           print little_brother
           print big_brother

print "1"
