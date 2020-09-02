def main():
    print("Hello! Enter the length of your list: ", end="")
    list_length = get_list_length()

    print("Enter your list!")
    numbers = get_list(list_length)

    textfile = open('result.txt', 'w')
    print("Your list: ", end="")
    print_list(numbers)
    textfile.write("Your list: ")
    print_list_in_file(numbers, textfile)

    print("Format list: ", end="")
    format_list(numbers)
    print_list(numbers)
    textfile.write("Format list: ")
    print_list_in_file(numbers, textfile)

    print("Ascending list: ", end="")
    sort_list(numbers, desc=False)
    print_list(numbers)
    textfile.write("Ascending list: ")
    print_list_in_file(numbers, textfile)

    print("Descending list: ", end="")
    sort_list(numbers)
    print_list(numbers)
    textfile.write("Descending list: ")
    print_list_in_file(numbers, textfile)

    textfile.close()


def format_list(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 0.13


def sort_list(numbers, desc=True):
    if desc:
        sort_list_desc(numbers)
    else:
        sort_list_asc(numbers)


def sort_list_asc(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp


def sort_list_desc(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] < numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp


def get_list_length():
    list_length = input()

    while not is_int(list_length):
        print_error_message()
        list_length = input()

    list_length = int(list_length)

    return list_length


def get_list(list_length):
    numbers = []

    for i in range(list_length):
        list_element = input()
        while not is_float(list_element):
            print_error_message(type_int=False)
            list_element = input()

        numbers.append(float(list_element))

    return numbers


def is_float(string):
    if not is_int(string):
        try:
            float(string)
        except ValueError:
            return False
    return True


def is_int(string):
    if string.isdigit():
        return True
    return False


def print_error_message(type_int=True):
    if type_int:
        print("Please enter an integer!")
    else:
        print("Please enter a decimal!")


def print_list(numbers):
    for number in numbers:
        print("{0:.2f}".format(number), end=" ")
    print()


def print_list_in_file(numbers, file):
    for number in numbers:
        file.write("{0:.2f} ".format(number))
    file.write("\n")


if __name__ == "__main__":
    main()
