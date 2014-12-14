def smallest_number():
    num = 20
    while True:
        for x in reversed(range(2, 21)):
            if num%x != 0:
                break
            if x == 2:
                return num
        num += 20

print smallest_number()    
            
