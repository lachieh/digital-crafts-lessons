
import sys
xr = 10

for x in xrange (0,xr):
    spaces = xr - x - 1
    stars = x * 2 + 1
    for y in xrange (0, spaces):
         sys.stdout.write(" ")
    for z in xrange(0, stars):
        sys.stdout.write("*")
    print ""
