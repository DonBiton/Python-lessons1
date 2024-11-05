import os


def input_int(text):
    x = input(text)
    if not (x.replace('.', '').isdigit()):
        print("Ошибка, вводи целые числа!")
        x = input(text)
    return int(x)


# 1
abstract_file = open('article.txt', 'r', encoding='utf-8')


def read_last(lines, file):
    if not lines >= 0:
        print('Число строк должно быть больше нуля')
        exit()
    abstract_file = open(file, 'r', encoding='utf-8')
    rows = abstract_file.readlines()
    last_rows = rows[-lines:]
    for row in last_rows:
        print(row, end='')
    return print(' ')


amount_of_last_lines = input_int("Количество последних строк: ")
read_last(amount_of_last_lines, 'article.txt')
abstract_file.close


# 2

def print_docs(directory):
    if not os.path.exists(directory):
        print(f"Директория '{directory}' не найдена.")
        return
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Если это директория, рекурсивно вызываем функцию
        if os.path.isdir(item_path):
            print(f"Директория: {item_path}")
            print_docs(item_path)
        else:
            print(f"Файл: {item_path}")


# print(os.getcwd())
# path = r'C:\Users\Miha1\OneDrive\Documents\Informatic\Python-lessons1\1\HT7>'
# print(path)
print_docs(r'C:\Users\Miha1\OneDrive\Documents\Informatic\Python-lessons1\1')

# 3


def longest_words(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    text = file.read()
    print(text)
    words = text.split()
    if words == []:
        print("Файл пустой")
        exit()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words


a = longest_words('article.txt')
print(a)

# 4


def redactor_txt():
    filename = input(
        'Введите имя файла (без расширения и не символы: \/:*?"<>|) ')
    special_symbol = '☺'
    filename += ".txt"
    file = open(filename, 'w', encoding='utf-8')
    while True:
        line = input("Вводите строку: ")
        if line == '' or special_symbol in line:
            break
        file.write(line + '\n')
    file.close()


redactor_txt()
