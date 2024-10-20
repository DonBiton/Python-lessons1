def input_int(text):
    x = input(text)
    if not (x.replace('.', '').isdigit()):
        print("Ошибка, вводи целые числа!")
        x = input(text)
    return int(x)


def creator_matrix(amount_str, amount_column):
    arr = list()
    for i in range(amount_str):
        brr = list()
        for i in range(amount_column):
            brr.append(input_int('Введите элемент матрицы: '))
        arr.append(brr)
    return arr


# 5
amount_str = input_int('Введите количество строк: ')
size_str = input_int('Введите количество столбцов: ')
matrix = creator_matrix(amount_str, size_str)
print(matrix)
min_str = 10_000
max_str = -10_000

for i in range(len(matrix)):
    a = sum(matrix[i])
    max_str = max(max_str, a)
    if a == max_str:
        print_max_str = matrix[i]
    min_str = min(min_str, a)
    if a == min_str:
        print_min_str = matrix[i]
print(f'наибольший ряд: {max_str} {print_max_str}')
print(f'наименьший ряд: {min_str} {print_min_str}')

# 6
amount_str = input_int('Введите количество строк: ')
size_str = input_int('Введите количество столбцов: ')
matrix = creator_matrix(amount_str, size_str)
print(matrix)
# Проверяем уникальность
k = 0
unique_matrix = set()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        unique_matrix.add(matrix[i][j])
        k += 1
if k != len(unique_matrix):
    print("Матрица не уникальна")
    exit()
for i in range(len(matrix)):
    min_el = min(matrix[i])
    for j in range(len(matrix[i])):
        if min_el % 2 == 0 and min_el == matrix[i][j]:
            matrix[i][j] = 0
        elif min_el % 2 == 1 and min_el == matrix[i][j]:
            matrix[i][j] = 1
print(matrix)
