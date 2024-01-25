a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a and c + a > b:
    print(True)
else:
    print(False)


a = int(input())
if a % 2 == 0:
    print(True)
else:
    print(False)


a = int(input())
b = int(input())
c = int(input())
if a + b > c:
    print(True)
elif a + b < c:
    print(False)


a = int(input())
b = int(input())
if a > b:
    print(True)
elif a < b:
    print(False)


a = input("login:")
b = input("password:")
if a == ("user") and b == ("qwerty"):
    print("Authentication completed")
elif a != ("user") and b != ("qwerty"):
    print("Invalid Login or Password")


a = int(input("Insert amount in KZT:"))
b = input("Choose currency: [1]USD, [2]EUR, [3]RUB:")
u = a / 420
if b == ("1"):
    print(a / 420)
elif b == ("2"):
    print(a / 510)
elif b == ("3"):
    print(a / 5.8)


a = int(input())
b = int(input())
c = int(input())
if a + b < c:
    print(True)
elif a + b > c:
    print(False)
