sum = 0
fib1 = 1
fib2 = 2

while fib2 < 4000000:
    if fib2%2 == 0:
        sum += fib2
    newfibsum = fib1 + fib2
    fib1 = fib2
    fib2 = newfibsum

print sum
