#Cначала мы принимаем числа в переменную а работая через .input() но так как нужно чтобы пользаветель ввел несколько значений мы также используем .split().
a = input().split()
#Далее работаем через len() чтобы узнать индексы чисел введенных пользователем.
if len(a) == 2:
    #Отчет в Пайтоне начинается с 0 поэтому наше первое число имеет индекс 0 а второе 1. Осталось лишь узнать сумму и разницу чисел.
    b = int(a[0])
    c = int(a[1])
    s = b + c
    g = b - c
    #Выводим результат
    print("Сумма равна:", s, "Разница равна:", g)


#Тут мы используем команду range чтобы выделить определенный диапозон чисел и уровнение чтобы выбрать только четные числа.
#А чтобы выбрать нечетные мы просто меняем РАВНО на НЕРАВНО а именно b % 2 != 0
a = [b for b in range (4, 31) if b % 2 == 0]
print(a)


import math
#Берем данные от пользователя
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
#Создаем функция для вычесления расстояния между точками.
def distance(x1, y1, x2, y2):
    X = x2 - x1
    Y = y2 - y1
    #Вычисление расстояния с использованием теоремы Пифагора и с библеотекой MATH
    b = math.sqrt(X ** 2 + Y ** 2)
    return b
# Вызов функции и вывод результата
c = distance(x1, y1, x2, y2)
print("Расстояние:", c)


def f(a, n):
    result = 1
    if n >= 0:
        for _ in range(n):
            result *= a
    else:
        for _ in range(abs(n)):
            result /= a
    return result
a = int(input())
n = int(input())
result = f(a, n)
print(f"{result}")


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
base = float(input())
exponent = int(input())
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")