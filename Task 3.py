def task3(text):
    answer = ""
    good = True
    for i in text:
        if i == ')' or i == '(':
            good = not good
        else:
            if good:
                answer = answer + i
    return answer
print("Введите строку со скобочками")
print(task3(input()))