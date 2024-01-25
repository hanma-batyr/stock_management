list = [10, 20, 30, 40]


def sum_list(x):
    if not x:
        return 0
    else:
        return x[0] + sum_list(x[1:])


sum = sum_list(list)
print(sum)


def recrusive(list, element, start=0, end=None):
    if end is None:
        end = len(list) - 1

    if start > end:
        return False

    middle_index = (start + end) // 2
    middle_element = list[middle_index]

    if middle_element == element:
        return True
    elif middle_element < element:
        return recrusive(list, element, middle_index + 1, end)
    else:
        return recrusive(list, element, start, middle_index - 1)


sort_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11
a = recrusive(sort_list, target)
print(a)


def digit_sum(x):
    return sum(int(x) for x in str(x))


list = [55, 22, 33, 11, 44]
sort_list = sorted(list, key=digit_sum)
print(sort_list)


def vowel_count(x):
    target = "aeiouAEIOU"
    return sum(1 for i in x if i in target)


list = ["baba", "ba", "bababa", "baaaaaaab", "b"]
sort_list = sorted(list, key=lambda x: vowel_count(x), reverse=True)
print(sort_list)


def binary_search(x, y):
    # Указываем границы начало и конца.
    start, end = 0, len(x) - 1
    # если начало больше конца то
    while start <= end:
        # Вычесляем индекс среднего элемента и получаем его значение
        middle_index = (start + end) // 2
        middle_element = x[middle_index]

        if middle_element == y:
            # Возвращаем индекс.
            return middle_index
        # создаем новый список и смещаем начало вправо от элемента
        # так как числа больше среднего элемента
        elif middle_element < y:
            start = middle_index + 1
        # создаем список и смещаем начало конец влево от элемента
        # так как числа меньше среднего элемента
        else:
            end = middle_index - 1
    # Число не найдено, возвращаем -1.
    return -1


sort_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(sort_list, target)
print(result)


def bubble_sort(x):
    # Получаем количество элементов в списке.
    elements = len(x)

    # Проходы по списку
    for i in range(elements - 1):
        # сравниваем и переставляем соседние элементы
        # после каждого прохода максимальный элемент встает в конец списка
        for j in range(elements - 1 - i):
            # cравниваем соседние элементы.
            if x[j] > x[j + 1]:
                # eсли текущий элемент больше следующего, меняем их местами
                x[j], x[j + 1] = x[j + 1], x[j]


list = [6, 4, 7, 5, 3, 8, 2, 1, 9]
bubble_sort(list)
print(list)
