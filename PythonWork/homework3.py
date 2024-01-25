a= [1, 2, 3, 4, 5, 6, 7, 8, 9]
b= a[1::3]
print(b)


a= "batyrzhan"
b= "r"
print(a.find(b))


a= "Пайтон очень папулярный язык"
b= "Пайтон"
print(a.startswith(b))


a= "12234batyrzhan"
print(a.isdigit())


a= ["python", "java","JavaScript"]
print(" ".join(a))


a= "Пайтон очень папулярный язык"
b= "Пайтон"
print(a.endswith(b))


a= "12234batyrzhan"
print(a.isalnum())


a= "python java JavaScript".split()[1]
print(a)


a= {"Python", "java", "JavaScript",}
b= {"html", "css", "c++", "Python"}
print(a.intersection(b))


a= {"Python", "java", "c++", "JavaScript",}
b= {"html", "css", "c++", "Python"}
print(a.union(b))


a= {"Python", "java", "c++", "JavaScript",}
b= {"html", "css", "c++", "Python"}
print(a.difference(b))


a= set()
a.update(input().split())
print(a)
b= next(iter(a),None)
a.discard(b)
print(a)


a= ["1", "2", "3", "4", "5"]
b= ["2", "7", "6", "4", "9"]
c= a+b
g= set(c)
print(g)