def task2(vector):
    for i in range(len(vector)):
        for j in range(len(vector)-1):
            if vector[j]>vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector
print("Введите массив для сортировки через пробел:")
print(task2(list(map(int, input().split()))))