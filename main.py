def square(side):
    per = side * 4
    squ = side ** 2
    diag = (2 * (side ** 2)) ** 0.5

    return per, squ, diag

s = input("Введите сторону квадрата") # Внес изменения в ветке test

print(square(s)) # Внес изменения в ветке test