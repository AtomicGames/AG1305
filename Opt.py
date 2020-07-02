import random

# индекс минимального элемента
def index_of_min(array):
    imin = 0

    for i, value in enumerate(array):
        if value < array[imin]: # если число меньше минимального
            imin = i # обновляем индекс

    return imin # возвраащем индекс

# индекс элемента
def index_of(array, search_value):
    for i, value in enumerate(array):
        if value == search_value: # если нашли значение
            return i # возвраащем индекс

    return -1 # не нашли

# сортировка массива
def sort_array(array):
    for i in range(1, len(array)):
        tmp = array[i] # запоминаем текущий элемент
        j = i

        # сдвигаем элементы, для освобождения места под вставляемый элемент
        while (j > 0) and (tmp < array[j - 1]):
            array[j] = array[j - 1]
            j-= 1

        array[j] = tmp # вставляем элемент в найденное место

# нахождение самой длинной последовательности одинаковых элементов
def find_sequence(array):
    max_start = 0
    max_length = 1

    i = 1
    curr_length = 1
    curr_start = 0

    while i < len(array):
        if array[i] == array[i - 1]:
            curr_length += 1
        else:
            if curr_length > max_length:
                max_length = curr_length
                max_start = curr_start

            curr_start = i
            curr_length = 1

        i += 1

    return max_start, max_length

# поиск трёх наибольших элементов массива
def find_maxs(array):
    if len(array) < 3:
        raise ValueError("Array too little")

    maxs = [ array[0], array[1], array[2] ]
    sort_array(maxs) # сортируем максимумы

    for i in range(3, len(array)):
        if array[i] > maxs[2]:
            maxs[0] = maxs[1]
            maxs[1] = maxs[2]
            maxs[2] = array[i]
        elif array[i] > maxs[1]:
            maxs[0] = maxs[1]
            maxs[1] = array[i]
        elif array[i] > maxs[0]:
            maxs[0] = array[i]

    return maxs # возвраащем максимумы

# сравнение массивов
def compare_arrays(array1, array2):
    if len(array1) < len(array2):
        return 1

    if len(array1) > len(array2):
        return -1

    for i in range(len(array1)):
        if array1[i] < array2[i]:
            return 1

        if array1[i] > array2[i]:
            return -1

    return 0 # массивы совпадают

# заполнение массива случайными числами
def fill_random(n, a, b):
    return [random.randint(a, b) for i in range(n)]

# ввод с клавиатуры
def read_from_keyboard():
    return [int(arg) for arg in input("Enter values: ").split()]

# режим ввода массива
def get_mode(message):
    mode = input(message)

    while mode != "random" and mode != "keyboard":
        mode = input("Invalid mode, try again: ")

    return mode

# получение массива
def get_array(mode):
    if mode == "keyboard":
        return read_from_keyboard()

    n = int(input("Enter size: "))
    a = int(input("Enter left border of random: "))
    b = int(input("Enter right border of random: "))

    return fill_random(n, a, b)

def main():
    mode = get_mode("Select input mode (random / keyboard) for first array: ")
    array1 = get_array(mode)
    mode = get_mode("Select input mode (random / keyboard) for second array: ")
    array2 = get_array(mode)

    value = int(input("Enter value for find: "))

    print("Array1: ", array1)
    print("Index of min: ", index_of_min(array1))
    print("Index of " + str(value) + ": ", index_of(array1, value))
    start, length = find_sequence(array1)
    print("Sequence: ", array1[start:start+length])
    print("Three max: ", find_maxs(array1))
    sort_array(array1)
    print("Sorted:", array1)

    print("\nArray2: ", array2)
    print("Index of min: ", index_of_min(array2))
    print("Index of " + str(value) + ": ", index_of(array2, value))
    start, length = find_sequence(array2)
    print("Sequence: ", array2[start:start+length])
    print("Three max: ", find_maxs(array2))
    sort_array(array2)
    print("Sorted:", array2)

    print("Compare('1'- if array1 < array2 or array1[i] < array2[i], '-1' - if if array1 > array2 or array1[i] > array2[i] ): ", compare_arrays(array1, array2))

main()