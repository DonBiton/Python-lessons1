def input_int(text):
    x = input(text)
    if not (x.replace('.', '').isdigit()):
        print("Ошибка, вводи целые числа!")
        x = input(text)
    return int(x)
#1
# abstract_file = open('article.txt', 'r', encoding='utf-8')

# def read_last(lines, file):
#     if not lines >= 0 :
#         print('Число строк должно быть больше нуля')
#         exit()
#     abstract_file = open(file, 'r', encoding='utf-8')
#     rows = abstract_file.readlines()
#     last_rows = rows[-lines:]
#     for row in last_rows:
#         print(row, end='')
#     return print(' ')

# amount_of_last_lines = input_int("Количество последних строк: ")
# read_last(amount_of_last_lines,'article.txt')
# abstract_file.close

    
#2
import os
def print_docs(directory):
    # Проверяем, существует ли директория
    if not os.path.exists(directory):
        print(f"Директория '{directory}' не найдена.")
        return
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Если это директория, рекурсивно вызываем функцию
        if os.path.isdir(item_path):
            print(f"Директория: {item_path}")
            print_docs(item_path)  # Рекурсивный вызов
        else:
            print(f"Файл: {item_path}")

# print(os.getcwd())
# path = r'C:\Users\Miha1\OneDrive\Documents\Informatic\Python-lessons1\1\HT7>'
# print(path)
print_docs(r'C:\Users\Miha1\OneDrive\Documents\Informatic\Python-lessons1\1')

#3