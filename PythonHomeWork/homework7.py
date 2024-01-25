import math

def f(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Введите корректное число.")

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '**': lambda x, y: x ** y,
    'sqrt': lambda x: math.sqrt(x),
    'sin': lambda x: math.sin(math.radians(x)),
    'cos': lambda x: math.cos(math.radians(x)),
    'tan': lambda x: math.tan(math.radians(x)),
    'factorial': factorial,
    'fibonacci': fibonacci
}

while True:
    print("Доступные операции:", ", ".join(operations.keys()))
    operation = input("Выберите операцию (или 'exit' для выхода): ")

    if operation == 'exit':
        break

    if operation in operations:
        try:
            if operation in ['factorial', 'fibonacci']:
                number = f("Введите число: ")
                result = operations[operation](number)
            else:
                num1 = f("Введите первое число: ")
                num2 = f("Введите второе число: ")
                result = operations[operation](num1, num2)

            print(f"Результат: {result}")
        except ZeroDivisionError:
            print("Деление на ноль невозможно.")
    else:
        print("Некорректная операция. Попробуйте еще раз.")


a = input()
b = list(map(int, a.split()))
c = list(filter(lambda x: x > 10, b))
print(c)

a = input()
b = lambda x: x.upper()
c = b(a)
print(c)


a = input().split()
b = list(filter(lambda x: len(x) > 5, a))
print(b)



a = list(map(int, input().split()))
b = list(map(lambda x: x * 2, a))
print(b)
