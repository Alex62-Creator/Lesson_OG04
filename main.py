def square(side):
    per = side * 4
    squ = side ** 2
    diag = (2 * (side ** 2)) ** 0.5

    return per, squ, diag

print(square(5))