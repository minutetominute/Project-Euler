import math

def is_prime(val):
    counter = 2
    while counter <= math.sqrt(val):
        if val%counter == 0:
            return False
        counter+=1
    return True

list = []
counter = 2

while len(list) < 10001:
    if is_prime(counter):
        list.append(counter)
    counter += 1

print len(list)
print list[-1]
