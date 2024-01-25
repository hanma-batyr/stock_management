def quick_sort(arr):
    # Если массив содержит 1 элемент или меньше, он считается отсортированным
    if len(arr) <= 1:
        return arr
    else:
        # Выбор опорного элемента (первый элемент массива)
        pivot = arr[0]
        
        # Создание массива less для элементов, меньших или равных опорному
        less = [x for x in arr[1:] if x <= pivot]
        
        # Создание массива greater для элементов, больших опорного
        greater = [x for x in arr[1:] if x > pivot]
        
        # Рекурсивная сортировка для подмассивов less и greater
        return quick_sort(less) + [pivot] + quick_sort(greater)

unsorted_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = quick_sort(unsorted_array)
print(sorted_array)
 

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid 
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def filter_and_sort_strings(input_list):
    filtered_list = [s for s in input_list if s and s[0].isupper()]
    sorted_list = sorted(filtered_list)
    return sorted_list


numbers = [8, 3, 12, 5, 6, 7, 10, 1, 2, 4]

filtered_and_sorted = sorted(filter(lambda x: x % 2 == 0, numbers))

print(filtered_and_sorted)


def filter_and_sort_words(input_words):
    filtered_words = [word for word in input_words if len(word) > 5]
    sorted_words = sorted(filtered_words, key=len)
    return sorted_words
