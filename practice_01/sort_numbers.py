"""
    Алгоритм работы программы:
    1. Производится ввод количества элементов в списке
       с проверкой на корректность введенного значения.
    2. Производится последовательный ввод элементов списка
       с проверкой на корректность введенного значения.
    3. Введенный лист сохраняется в файл result.txt в строке "Your list:"
    4. Полученный список умножается на 0.13 и печатается в текстовый файл
       в строке "Format list:"
    5. Отформатированный лист сортируется по возрастанию и печатается в файл
    6. Отформатированный лист сортируется по убыванию и печатается в файл

    Вся информация записывается в txt-файл, т.к. этот формат предоставляет простую и
    понятную структуру для чтения и записи информации, и в случае необходимости
    можно дописать простой парсер, чтобы считать нужную информацию.
"""

# Константы приложения
DEFAULT_MULTIPLIER = 0.13

"""
    Функции format_list, sort_list, sort_list_asc, sort_list_desc отвечают
    за форматирование введенного списка
"""


def format_list(numbers):
    # Умножение введенного списка на 0.13
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * DEFAULT_MULTIPLIER


def sort_list(numbers, desc=True):
    # Выбор типа сортировки в зависимости от параметра desc
    if desc:
        sort_list_desc(numbers)
    else:
        sort_list_asc(numbers)


def sort_list_asc(numbers):
    # Сортировка по возрастанию
    numbers.sort(reverse=False)


def sort_list_desc(numbers):
    # Сортировка по убыванию
    numbers.sort(reverse=True)


"""
    Функции get_list_length и get_list отвечают за ввод значений 
    в программу.
"""


def get_list_length():
    # Функция ввода длины
    list_length = input()

    # Проверка на корректность введенного значения
    while not is_int(list_length) and not is_positive(list_length):
        print_error_message()
        list_length = input()

    list_length = int(list_length)

    return list_length


def get_list(list_length):
    numbers = []

    # Ввод элементов списка с проверкой на корректность введенных значений
    for i in range(list_length):
        list_element = input()
        while not is_float(list_element):
            print_error_message(type_int=False)
            list_element = input()

        numbers.append(float(list_element))

    return numbers


"""
    Функции is_float, is_int, is_integer осуществляют проверку
    принимаемых значений.
"""


def is_float(string):
    # Проверка числа на тип float
    if not is_int(string):
        try:
            float(string)
        except ValueError:
            return False
    return True


def is_int(string):
    # Проверка числа на тип int
    if string.isdigit():
        return True
    return False


def is_positive(string):
    # Проверка на положительное число
    if int(string) > 0:
        return True
    return False


"""
    Функции print_error_message и print_list предназначены для вывода
    информации, которая возникает в ходе использования программы
    пользователем.  
"""


def print_error_message(type_int=True):
    if type_int:
        print("Please enter a positive integer!")
    else:
        print("Please enter a number!")


def print_list(numbers, file):
    for number in numbers:
        file.write("{0:.2f} ".format(number))
        print("{0:.2f}".format(number), end=" ")
    file.write("\n")
    print()


"""
    Main - главная функция программы, связывающая все выше описанные функции.
"""


def main():
    print("Hello! Enter the length of your list: ", end="")
    list_length = get_list_length()

    print("Enter your list!")
    numbers = get_list(list_length)

    # Открытие текстового файла на запист
    textfile = open('result.txt', 'w')

    print("Your list: ", end="")
    textfile.write("Your list: ")
    print_list(numbers, textfile)

    print("Format list: ", end="")
    textfile.write("Format list: ")
    format_list(numbers)
    print_list(numbers, textfile)

    print("Ascending list: ", end="")
    textfile.write("Ascending list: ")
    sort_list(numbers, desc=False)
    print_list(numbers, textfile)

    print("Descending list: ", end="")
    textfile.write("Descending list: ")
    sort_list(numbers)
    print_list(numbers, textfile)

    # Закрытие файла
    textfile.close()


# Вход в программу
if __name__ == "__main__":
    main()
