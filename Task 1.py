def task1(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print("Введите целое чисто от 0 до 1000")
print(task1(int(input())))