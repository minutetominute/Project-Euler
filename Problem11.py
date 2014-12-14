import string



num_grid_file = open('Problem11Data', 'r')

num_grid = []

line_list = string.split(num_grid_file.read(), '\n')

for line in line_list:
    string_list = []
    num_list = []
    string_list = string.split(line, ' ')
    for num in string_list:
        num_list.append(int(num))
    num_grid.append(num_list)

greatest_product = 0

def contains_negative(list):
    for item in list:
        if item < 0:
            return True
    return False

def products(x, y):
    list = []
    list.append(product_up(x, y))
    list.append(product_down(x, y))
    list.append(product_right(x, y))
    list.append(product_left(x, y))
    list.append(product_diag_up_left(x, y))
    list.append(product_diag_up_right(x, y))
    list.append(product_diag_down_left(x, y))
    list.append(product_diag_down_right(x, y))
    return list

def product_up(x, y):
    product = 1
    try:
        if contains_negative(range(x-3, x+1)):
            return 0
        for x_index in range(x-3, x+1):
            product *= num_grid[x_index][y]
    except IndexError:
        return 0
    return product

def product_down(x, y):
    product = 1
    try:
        if contains_negative(range(x, x+4)):
            return 0
        for x_index in range(x, x+4):
            product *= num_grid[x_index][y]
    except IndexError:
        return 0
    return product

def product_right(x, y):
    product = 1
    try:
        if contains_negative(range(y, y+4)):
            return 0
        for y_index in range(y, y+4):
            product *= num_grid[x][y_index]
    except IndexError:
        return 0
    return product
    
def product_left(x, y):
    product = 1
    try:
        if contains_negative(range(y-3, y+1)):
            return 0
        for y_index in range(y-3, y+1):
            product *= num_grid[x][y_index]
    except IndexError:
        return 0
    return product

def product_diag_up_left(x, y):
    product = 1
    try:
        if contains_negative(range(x-3, x+1)):
            return 0
        if contains_negative(range(y-3, y+1)):
            return 0
        y_index = y
        for x_index in range(x-3, x+1):
            product *= num_grid[x_index][y_index]
            y_index-=1
    except IndexError:
        return 0
    return product

def product_diag_up_right(x, y):
    product = 1
    try:
        if contains_negative(range(x-3, x+1)):
            return 0
        if contains_negative(range(y, y+4)):
            return 0
        y_index = y
        for x_index in range(x-3, x+1):
            product *= num_grid[x_index][y_index]
            y_index+=1
    except IndexError:
        return 0
    return product

def product_diag_down_left(x, y):
    product = 1
    try:
        if contains_negative(range(y-3, y+1)):
            return 0
        if contains_negative(range(x, x+4)):
            return 0
        y_index = y
        for x_index in range(x, x+4):
            product *= num_grid[x_index][y_index]
            y_index-=1
    except IndexError:
        return 0
    return product

def product_diag_down_right(x, y):    
    product = 1
    try:
        if contains_negative(range(x, x+4)):
            return 0
        if contains_negative(range(y, y+4)):
            return 0
        y_index = y
        for x_index in range(x, x+4):
            product *= num_grid[x_index][y_index]
            y_index+=1
    except IndexError:
        return 0
    return product
    
for x in range(0, 20):
    for y in range(0, 20):
        product_list = products(x, y)
        for product in product_list:
            if product > greatest_product:
                greatest_product = product

print greatest_product
