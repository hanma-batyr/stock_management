#1
age = 21


#2
a = [1, "a", True]
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))



#4  
numbers = [12, 41, 511, 2, 4]
print(max(numbers))
print(min(numbers))
num = list(filter(lambda x: x % 2 == 0, numbers))
print(num)


#5
num = int(input())
float_num = float(input())
b = num / float_num
print(b)


#6
num = int(input())
def n(x):
    if x % 2 == 0 and x > 0:
        print(x)
    else: 
        print("число не подходить")
n(num)


#7
age = int(input())
def f(x):
    if x > 18: 
        print("вы совершеннолетний. вам можно")
    else:
        print("вы не совершеннолетний. вам можно но за это вас накажут)")
f(age)


#8
def summa (x, y):
    print(x + y)
one = int(input())
two = int(input())
summa (one, two)


#9
a = list(map(int, input()))
b = list(map(lambda x: x ** 2, a))
print(b)


#10
Peopls = {"марк": 16, "маркк": 20, "марккк": 6, }
print(Peopls)


#11
a = input()
b = a.count(a)
print(b)


#13
num = int(input())
def tab(x):
    print(x * 1)
    print(x * 2)
    print(x * 3)
    print(x * 4)
    print(x * 5)
    print(x * 6)
    print(x * 7)
    print(x * 8)
    print(x * 9)
    print(x * 10)
tab(num)


#14
try:
    user = int(input())
except ValueError:
    print("Введите число")


#15
a = "fffff"
b = "bbbbbbbb"
print(len(a))
print(len(b))
c = a + b
print(len(c))