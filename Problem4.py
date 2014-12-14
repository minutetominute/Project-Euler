largestx = 0
largesty = 0
for x in reversed(range(100, 1000)):
    for y in reversed(range(100, 1000)):
        if str(x*y) == str(x*y)[::-1]:
            if x*y > largestx*largesty:
                largestx = x
                largesty = y
print "{0} * {1}".format(largestx, largesty)            
