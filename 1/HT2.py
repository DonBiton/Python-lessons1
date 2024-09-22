# 1
a, b = input('Введите 2 вещественных числа через пробел: ').split()
if not (a.replace('.', '').isdigit()) or not (b.replace('.', '').isdigit()):
    print("Ошибка, вводи числа!")
    exit()
a, b = float(a), float(b)
if b == 0:
    print("Ошибка, деление на ноль")
else:
    print(a/b)

# 2
a = input('Введите сумму покупки: ')
if not (a.replace('.', '').isdigit()):
    print("Ошибка, вводи числа!")
    exit()
a = float(a)
if a > 20:
    print("Итоговая стоимость:", round(
        a-a*0.35, 2), 'Скидка:', round(a*0.35, 2))
else:
    print("Итоговая стоимость:", round(a, 2), 'Скидка: 0')

# 3

a = input('Введите число от 1 до 12: ')
if not (a.isdigit()):
    print("Вводите число от 1 до 12!")
    exit()
a = int(a)
if not (1 <= a <= 12):
    print("Вводите число от 1 до 12!")
    exit()
if a >= 3 and a <= 5:
    if a == 3:
        print("Весна, Март")
    elif a == 4:
        print("Весна, Апрель")
    else:
        print("Весна, Май")
elif a >= 6 and a <= 8:
    if a == 6:
        print("Лето, Июнь")
    elif a == 7:
        print("Лето,июль")
    else:
        print("Лето, август")
elif a >= 9 and a <= 11:
    if a == 9:
        print("Осень, Сентябрь")
    elif a == 10:
        print("Осень, Октябрь")
    else:
        print("Осень, Ноябрь")
else:
    if a == 12:
        print('Зима, Декабрь')
    elif a == 1:
        print("Зима, Январь")
    else:
        print("Зима, Февраль")

# 3.1

a = input('Введите число от 1 до 12: ')
if not (a.isdigit()):
    print("Вводите число от 1 до 12!")
    exit()
a = int(a)
if not (1 <= a <= 12):
    print("Вводите число от 1 до 12!")
    exit()
months = ["Зима, Январь", "Зима, Февраль", "Весна, Март", "Весна, Апрель", "Весна, Май", "Лето, Июнь",
          "Лето,июль", "Лето, август", "Осень, Сентябрь", "Осень, Октябрь", "Осень, Ноябрь", 'Зима, Декабрь']
print(months[a-1])
