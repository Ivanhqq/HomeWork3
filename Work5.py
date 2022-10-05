# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)


x = int(input('Введи число: '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fiba(n):
    if n in [1, 2]:
        return 1
    else:
        return fiba(n+2) - fiba(n+1)


list1 = []
for i in range(-x, 1):
    list1.append(fiba(i))

for i in range(1, x+1):
    list1.append(fib(i))


print(list1)
