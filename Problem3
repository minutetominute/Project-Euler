import math

def is_prime(val):
    counter = 2
    while counter < math.sqrt(val):
        if val%counter == 0:
            return False
        counter+=1
    return True

def largest_prime_factor(val):
    counter = 1
    largest_prime = 0
    while counter < math.sqrt(val):
        if val%counter == 0 and is_prime(counter):
            largest_prime = counter
            print largest_prime
        counter+=1
    print largest_prime

largest_prime_factor(600851475143)
