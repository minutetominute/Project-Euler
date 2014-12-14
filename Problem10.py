import math

def is_prime(val):
    counter = 2
    while counter <= math.sqrt(val):
        if val%counter == 0:
            return False
        counter+=1
    return True

primesum = 0

for x in range(2, 2000001):
    if is_prime(x):
        primesum += x

print primesum
        
