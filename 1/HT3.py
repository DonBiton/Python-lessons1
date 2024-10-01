# 1
a = input('Введите число от 2 до 100: ')
if not (a.isdigit()):
    print("Вводите число от 1 до 100!")
    exit()
a = int(a)
if not (2 <= a <= 100):
    print("Вводите число от 1 до 100!")
    exit()
sum1 = 0
for i in range(1, a+1):
    sum1 = sum1 + i**3
print(sum1)
# 2
for i in range(1, 10):
    row = str(i).rjust(3)
    for j in range(1, 10):
        row = row + " " + str(i * j).rjust(3)
    print(row)
