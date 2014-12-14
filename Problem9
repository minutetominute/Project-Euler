import math
import sys

x = []
for c in range(0, 1001):
    for b in range(0, c):
        for a in range(0, b):
            if a*a + b*b == c*c:
                x.append((a, b, c))
                if x[-1][0] + x[-1][1] + x[-1][2] == 1000:
                    print x[-1]
                    print x[-1][0]*x[-1][1]*x[-1][2]
                    sys.exit()
