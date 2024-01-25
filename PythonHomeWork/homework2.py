a= input()
b= a[:a.find(' ')]
c= a[a.find(' ') + 1:]
print(c, b)


a= input()
b= a.count(" ")+1
print(b)


a= input()
b= a.replace("2020", "2023")
print(b)


a= input()
b = [int(num) for num in a.split()]
c = sum(num**2 for num in b)
print("Сумма квадратов чисел:", c)



a= input().split()
five= a.count("5")
four= a.count("4")
three= a.count("3")
two= a.count("2")
b= len(a)
c= (5 * five + 4 * four + 3 * three + 2 * two) / b if b > 0 else 0
print (five, four, three, two,)
print (f"{c: 2f}")


a= input()
b= a.replace ("2", "3")
print(b)