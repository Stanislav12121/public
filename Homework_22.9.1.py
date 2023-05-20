p = input("Введите последовательность любых чисел через пробел ") #запрашиваем у пользователя последовательность чисел

p = p.split() #создаем список из введенной последовательности

nums = list(map(int, p)) #преобразуем в числовой список

s = int(input("Введите любое число, которое входит в область введенной последовательности ")) #запрашиваем у пользователя любое число
while s > max(nums) or s < min(nums): #проверяем, чтобы введенное число входило в область чисел последовательности. Необходимо, чтобы скрипт не завершался ошибкой во время двоичного поиска
    s = int(input("Вы ввели некорректное число. Введите любое число, которое входит в область введенной последовательности "))

l = len(nums) #длина списка, необходима для определения правой границы в функции поиска

def sort(array): #функция сортировки вставками
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    print(array)

def binary_search(array, element, left, right): 
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует
        
    middle = (right+left) // 2 # находим середину
    if array[middle - 1] < element and array[middle] >= element: # если предыдущий элемент меньше нашего, а следующий больше или равен нашему
        return middle - 1 # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)
    
sort(nums) #выводим отсортированный список
print(binary_search(nums, s, 0, l)) #выводим индекс элемента, который меньше нашего
